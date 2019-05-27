/****************************************************
 * ROVIO  asservissement de position                *
 * Boucle ouverte sous PWM 0..255                   *
 * Boucle fermee : echelon position                 *
 * Jabvier 2017  - Jacques Tanoh                    *
****************************************************/
//
//-------------------------------------------------------------------------------
#include <PID_v1.h>
#include <Encoder.h>
// Codeur
int CHA_pin=2;
int CHB_pin=3;//4
// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(CHA_pin, CHB_pin);// 2  4 les interruptions  sont sur 2 et 3
//   avoid using pins with LEDs attached
//----------------------------------------------------------
//Moteur :
#define PIN_DIR 10   // direction moteur avance  B
#define PIN_COMMANDE 9 // power du moteur B  (c'est une PWM)
// shield moteur M+  = le blanc ; M- : le noir 

// ************************************************************************************
const int nb=120;  // nombre de points de mesure 120
const int Umot_mV=6000;
//
double Consigne, Mesure, Commande;  // grandeurs en points
//Valeur par defaut du PID
double ech, Kp=1.0, Ki=0, Kd=0;
PID myPID(&Mesure, &Commande, &Consigne, Kp, Ki, Kd, DIRECT);// ancienne position
long posinit;

void setup()
{
      pinMode(PIN_DIR, OUTPUT); 
      pinMode(PIN_COMMANDE, OUTPUT);
      pinMode(CHA_pin, INPUT);
      pinMode(CHB_pin, INPUT);   
      // initialisation port serie:
      Serial.begin(115200);     
}

void loop()
{
 int leChoix=choisirMenu(); 
 switch (leChoix) {
    case 1:
      BO();
      break;
    case 2:
      BF();
      break;
  }
 
}  
// -------------------------------------------------------------------
void BO()
{
         // Debut Boucle Ouverte
                int periode_echant=200; // periode echantillonnage
				int comPWM=0;
                Serial.println(F("***************************** "));
                Serial.println(F("ROVIO "));
                Serial.println(F("Asservissement de position  : essai en BO choix PWM"));
				// choix commande
				  Serial.println(F("  Entrer la commande en entier [0 ..255]"));
                bool OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {               
                        // recherche du prochain entier sur le port serie:
                        float iPWM = Serial.parseFloat();         
                        // recherche du caractere nouvelle ligne pour terminer                  
                        if (Serial.read() == '\n') {
                          // contraint la valeur dans un intervalle
                          comPWM = constrain(iPWM,0,255);    //limiter echelon              
                          // affiche :
                          Serial.print(F("  PWM= "));
                          OK=true;
                        } // fin if Serial
                     Serial.println("--------------------"); 

                   };// fin while Serial.available
                 }// fin while OK false               

				// fin choix commande
                Serial.println(F("   Vitesse en pt/s"));
                Serial.println(F("   (Entree pour demarrer et pour arreter)"));               
                OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {                
                                                // recherche du caractere nouvelle ligne pour terminer                   
                        if (Serial.read() == '\n') {
                          OK=true;
                           } // fin if Serial                    
                   };// fin while Serial.available
                 }// fin while OK false
                 // demarrage-------------------------------------------------------------
                 Consigne = 500; // 
                 myEnc.write(0);        
                 myPID.SetOutputLimits(-255, 255);
                 myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms   ******* 
 
                 //++++++++++++++++++++++++++++++++++              
                 //activation PID       
                 myPID.SetMode(AUTOMATIC);
                 myPID.SetTunings( 5,  0, 0);             
                 // ------------------------------  fin entree  
                 // lancement du mouvement 
                 bool calcule;
                 double date,date0,dateInit;
                 dateInit=millis();
                 date0=-1 ;              
                 Fait_PWM(int(comPWM));                  
                 posinit= myEnc.read();
                 double Mesure0=0;
                 Mesure=0;
                 float vitesse= 0;             
                 // Serial.println(F(" Entree pour arreter"));
                 // si quelque chose sur port serie,le lire :  
                 while (Serial.available() ==0) {                
                        Mesure=myEnc.read()-posinit;                   
                        date=millis()-dateInit;                              
                        calcule=myPID.Compute();
                        if (calcule) {     
                          vitesse=(Mesure-Mesure0)*1000./(date-date0);                                   
                          Mesure0=Mesure;
                          date0=date; 
                          Serial.print(vitesse,0);Serial.println(F(" pt/s"));                   
                         }     
                   
                  };// fin while Serial       
                 
                  myPID.SetMode(MANUAL);
                  Fait_PWM(0);
                  //while(true){}  // Rester dans boucle infinie
}

//--------------------------------------------------------------------
void BF()
{
        //  BF echelon position: 
                int periode_echant=10; // periode echantillonnage
                 Serial.println(F(" "));
                Serial.println(F(""));
                Serial.println(F("        Asservissement de position  :"));
                Serial.println(F(""));
                 // choix correcteur--------------------------------------------------------------------------                
                Serial.println(F("Correction : entrer Kp, Ki et Kd flottants positifs separes par des virgules"));
                Serial.println(F("Kp [1 .. 20] Ki[0 .. 5]  Kd[0 ..5]"));
               
                bool OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {                
                         // encore:
                        float iKp = Serial.parseFloat();
                        // encore:
                        float iKi = Serial.parseFloat();
                        // encore:
                        float iKd = Serial.parseFloat();            
                        // recherche du caractere nouvelle ligne pour terminer
                    
                        if (Serial.read() == '\n') {
                          iKp = constrain(iKp, 1, 20);    //limiter Kp
                          iKi =constrain(iKi, 0, 5);    // limiter Ki 
                          iKd =constrain(iKd, 0, 5);    // limiter Kd
                
                          // affiche :
                          Serial.print("Kp= ");
                          Serial.print(iKp);
                          Serial.print("    ");
                          Serial.print(" Ki= ");
                          Serial.print(iKi);
                          Serial.print("   ");
                          Serial.print(" Kd= ");
                          Serial.println(iKd);
                          OK=true;
                        } // fin if Serial
                     Serial.println(F("--------------------")); 
                     Kp=iKp;
                     Ki=iKi;
                     Kd=iKd;
                   };// fin while Serial.available
                 }// fin while OK false
                 // fin choix correcteur-------------------------------------------------------------
                  Serial.println(F("  Entrer une consigne de position en points [0 ..1000]"));
                OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {               
                        // recherche du prochain entier sur le port serie:
                        float iech = Serial.parseFloat();         
                        // recherche du caractere nouvelle ligne pour terminer                  
                        if (Serial.read() == '\n') {
                          // contraint la valeur dans un intervalle
                          ech = constrain(iech,0,1000);    //limiter echelon              
                          // affiche :
                          Serial.print(F("  Consigne= "));
                          Serial.print(ech);Serial.println(F("  points"));
                          OK=true;
                        } // fin if Serial
                     Serial.println("--------------------"); 

                   };// fin while Serial.available
                 }// fin while OK false               
                 //fin choix echelon
                 // +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                              
                 Consigne = ech; //         
                 myEnc.write(0);
                 myPID.SetOutputLimits(-255, 255);
                 myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms   ******* 
                 //++++++++++++++++++++++++++++++++++  
// où placer myPID.SetTunings	 ??			 
                 myPID.SetTunings( Kp,  Ki,  Kd);  				 
                 //activation PID       
                 myPID.SetMode(AUTOMATIC);
                 myPID.SetTunings( Kp,  Ki,  Kd);             
                 // ------------------------------  fin entree  
                 // lancement du mouvement 
                 int n= 0;
                 int resc[nb];  // avant  : double
                 double resm[nb]; //  avant : double
                 double rest[nb];//long unsigned
                 bool calcule;
                 double date,date0;
                 long posit;
                 date0=micros(); 
                 Commande=0;                    
                 posinit= myEnc.read();
                 while (n<nb) {
                    Mesure=myEnc.read()-posinit;                   
                    date=micros()-date0;                              
                    calcule=myPID.Compute();
              
                    if (calcule) {     
                        resm[n]=Mesure;
                        rest[n]=date;
                        resc[n]=Commande;                              
                        Fait_PWM(int(Commande));               
                        n++;                 
                     }
                  } // fin while n<nb
                  myPID.SetMode(MANUAL);
                  Fait_PWM(0); // arreter moteur
                 
                  Serial.print(F(" ; ; ; ; Correcteur: Kp= "));Serial.print(myPID.GetKp());
                  Serial.print(" Ki= ");Serial.print(myPID.GetKi());
                  Serial.print(" Kd=  ");Serial.println(myPID.GetKd()); 
                  Serial.print(F("; ; ; ;Consigne [pt] : "));Serial.println(Consigne);// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                  Serial.println(F("date;Consigne;Mesure;Umoteur"));
                  Serial.println(F("[s];[pt];[pt];[mV]"));
                  //Serial.print(0);Serial.print("; ");  Serial.print(0);Serial.print("; ");
                  //Serial.print(0);Serial.print("; ");//
                  //Serial.println(0);
                  n=0;
                  while (n<nb) {
                        Serial.print(double(rest[n])/1e6,4);Serial.print("; ");  Serial.print(int(Consigne));Serial.print("; ");
                        Serial.print(int(resm[n]));Serial.print("; ");//
                        Serial.println(resc[n]*6.0/255.0,0); // la tension alim est 6V
    
                        n++;
                  }// fin while n< nb
                  Serial.println();
                  Serial.println(F(" fini"));
                  //while(true){}
}
//-----------------------------------------------------------------------------
int choisirMenu()
{  
  Serial.println(F(""));
  Serial.println(F(" ********************************************"));
  Serial.println(F(" *      ROVIO Asservissement de position    *"));
  Serial.println(F(" ********************************************"));
  Serial.println(F("                                         v1"));
  Serial.println(F(""));
  Serial.println(F("Choix :"));
  Serial.println(F(" - Boucle Ouverte sous 6V             --->   1"));
  Serial.println(F(" - Boucle Fermee echelon de position  --->   2"));
  Serial.println(F("      (.... et Entree)"));
 
  bool OK=false;
  // MENU 
  //-------------------------Choix menu -----------------------------
  int choix;
      while(OK== false){
          // si quelque chose sur port serie,le lire :  
          while (Serial.available() > 0) {                
                // recherche du prochain entier sur le port serie:
                 choix = Serial.parseInt();         
                // recherche du caractere nouvelle ligne pour terminer                        
                if (Serial.read() == '\n') {
                    choix = constrain(choix, 0, 2);    //limiter choix  
                    OK=true;
                    } // fin if Serial
            
           };// fin while Serial.available
       }// fin while OK false
     return choix;
 }      
 
//-----------------------------------------------------------------------------

void Fait_PWM(int y)  // commande moteur
    { analogWrite(PIN_COMMANDE, 0);
      if (y <0) { digitalWrite(PIN_DIR,LOW);y=-y;}
      else{digitalWrite(PIN_DIR,HIGH);}
    analogWrite(PIN_COMMANDE, y);
     }
     
void attend(){;}   
