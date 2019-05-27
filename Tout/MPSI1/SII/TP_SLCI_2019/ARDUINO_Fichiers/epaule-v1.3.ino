/*********************************************************
 * Ericc axe lacet ou epaule  asservissement de vitesse  *
 * Boucle ouverte sous 24V                               *
 * Boucle fermee : echelon position                      *
 *  travail en degrés                                    *
 *  test initial                                         *
 * juin 2017  - Jacques Tanoh                            *
**********************************************************/
//
//-------------------------------------------------------------------------------
#include <PID_v1.h>
// Codeur
int CHA_pin=2;
int CHB_pin=13;//impose due
//----------------------------------------------------------
//Moteur :
#define PIN_DIR1 10   // in1   moteur
#define PIN_DIR2 11   // in2   moteur
#define PIN_COMMANDE 9 // power du moteur B  (c'est une PWM)
//#define PIN_FDC4 50 // signal fin de course poignet

// shield moteur M+  = le blanc ; M- : le noir 
// ************************************************************************************
const int nb=100;  // nombre de points de mesure 120
const int Umot_mV=24000;
const int periode_echant=10; // periode echantillonnage du PID
//
/*

Si la position au demarrage est < 25.4 alors fdc4 =1 sinon fdc4 =0
 */
const float points_par_degre=1851.85;
const long int pt_fdc=long(points_par_degre*(26.9-1.8));//-1.5
long posinit, pos_fdc=0;
long int le_zero=0;
double Consigne, Mesure, Commande;  // grandeurs en points
//Valeur par defaut du PID
double ech, Kp=0.0, Ki=0, Kd=0;
PID myPID(&Mesure, &Commande, &Consigne, Kp, Ki, Kd, DIRECT);// ancienne position


//?????????????????????????????????????????????????????????????????????????????????????????????????????? REG_TC0_CCR0 = 5;  //


const int ENCODER_SAMPLES_PER_SECOND = 1024;        // this will need to be tuned depending on your use case...
boolean uneFois=true;
boolean autorise=false;
boolean caMarche=false;
void setup()
{
      pinMode(PIN_DIR1, OUTPUT);
      pinMode(PIN_DIR2, OUTPUT);  
      pinMode(PIN_COMMANDE, OUTPUT);
      pinMode(CHA_pin, INPUT);
      pinMode(CHB_pin, INPUT); 
  
                // initialisation port serie:
                Serial.begin(115200);   
            // Setup Quadrature Encoder
            REG_PMC_PCER0 = PMC_PCER0_PID27
                          | PMC_PCER0_PID28
                          | PMC_PCER0_PID29;
          
            REG_TC0_CMR2 = TC_CMR_TCCLKS_TIMER_CLOCK4 
                         | TC_CMR_WAVE
                         | TC_CMR_ACPC_TOGGLE 
                         | TC_CMR_WAVSEL_UP_RC;
          
            REG_TC0_RC2 = F_CPU / 128 / ENCODER_SAMPLES_PER_SECOND;
            
            REG_TC0_CMR0 = TC_CMR_ABETRG
                         | TC_CMR_LDRA_EDGE
                         | TC_CMR_LDRB_EDGE 
                         | TC_CMR_ETRGEDG_EDGE 
                         | TC_CMR_CPCTRG;
          
// ************************************************************************
                // mode position
                REG_TC0_BMR = TC_BMR_QDEN
                            | TC_BMR_POSEN
                            | TC_BMR_EDGPHA;  
                // Set everything going
                REG_TC0_CCR0 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                REG_TC0_CCR1 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                REG_TC0_CCR2 = TC_CCR_CLKEN | TC_CCR_SWTRG;
                REG_TC0_CCR0 = 5;

le_zero = REG_TC0_CV0;;
;//Serial.println(TC_CCR_SWTRG);
Serial.println(F("Ericc epaule v1.2"));
Serial.println(F("*****************"));
}

bool verif()
{ bool reussi=false;
long int verPos0;
long int verPos45;
int fdc0;
int fdc45;
libereMoteur();
Serial.println(F("Tests avant mise en mouvements: ")); 
Serial.println(F("Mettre manuellement  ET LENTEMENT l'axe dans la position 0 degre et faire Entree"));
 bool OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {                
                                                // recherche du caractere nouvelle ligne pour terminer                   
                        if (Serial.read() == '\n') {
                          OK=true;
                           } // fin if Serial                    
                   };// fin while Serial.available
                 }// fin while OK false
                 // demarrage verif 0-------------------------------------------------------------                              
                 verPos0=MesurePosition();Serial.println(verPos0);
                 fdc0 =analogRead(A0);Serial.println(fdc0);
      
                Serial.println(F("Mettre manuellement ET LENTEMENT l'axe dans la position 45 degres et faire Entree"));
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
        
                // demarrage verif 0-------------------------------------------------------------                              
                 verPos45=MesurePosition();Serial.println(verPos45);
                 fdc45 =analogRead(A0);Serial.println(fdc45);
                 /*while (Serial.available() ==0) {                         
                  //----------------------------------------------------------                                              
                  ;};// fin while Serial       
                   */
/* Delta points entre 0 et 45 : 83900
 *  fdc 0  =369;
 *  fdc45  =996
 */
int resFdc=0 ;
int resCodeur=0;

if ( fdc0<500 and fdc45 > 900){resFdc=1;
Serial.println(F("Test Fin de course reussi "));}
else{Serial.println(F("Test Fin de course rate "));};
if( verPos45-verPos0 > 80000 and verPos45-verPos0 < 90000 ){ resCodeur=2;
Serial.println(F("Test Fin de codeur reussi "));}
else{Serial.println(F("Test codeur rate "));};
if (resCodeur+resFdc==3) 
  {reussi= true;
  Serial.println(F("Tests reussis , initialisation possible \n"));
  }
return reussi;
}

void loop()
{ 
  if (not(autorise)){caMarche=verif();}
  
  if (caMarche)
  {     autorise=true;
        if (uneFois ){ Initialisation_axe(); uneFois=false;} 
         int leChoix=choisirMenu(); 
         switch (leChoix) {
           case 0:
              Initialisation_axe();
              break;  
            case 1:
              BF();
              break;
            case 2:
              Codeur();
              break;
          }
  }
  else
  {
  Serial.println(" !!!!!!!!!!!!!  DEFAUT !!!!!!!!!!");
  
  while (true )
  {
    }  
}  
}
// -------------------------------------------------------------------
void BF()
{


  //  BF echelon position: 
                Serial.println(F(" "));
                Serial.println(F(""));
                Serial.println(F("        Asservissement de position  :"));
                Serial.println(F(""));
                 // choix correcteur--------------------------------------------------------------------------                
                Serial.println(F("Correction : entrer Kp, Ki et Kd flottants positifs separes par des virgules"));
                Serial.println(F("Kp [1 .. 100] Ki[0 .. 40]  Kd[0 .. 2]"));
               // 10 10 0.01
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
                          iKp = constrain(iKp, 0.1, 100);    //limiter Kp
                          iKi =constrain(iKi, 0, 40);    // limiter Ki 
                          iKd =constrain(iKd, 0, 2);    // limiter Kd
                
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
                  Serial.println(F("  Entrer la position a atteindre de degre [-45 ..60]"));
                OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {               
                        // recherche du prochain entier sur le port serie:
                        float iech = Serial.parseFloat();         
                        // recherche du caractere nouvelle ligne pour terminer                  
                        if (Serial.read() == '\n') {
                          // contraint la valeur dans un intervalle
                          ech = constrain(points_par_degre*iech,-83350,111200);    //limiter echelon              
                          // affiche :
                          Serial.print(F("  Consigne= "));
                          Serial.print(ech/points_par_degre,2);Serial.println(F("  degres"));
                          OK=true;
                        } // fin if Serial
                     Serial.println("--------------------"); 

                   };// fin while Serial.available
                 }// fin while OK false               
                 //fin choix echelon
                 // +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                              
                 Consigne = ech; //         
                 myPID.SetOutputLimits(-255000, 255000);
                 myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms   ******* 
                 //++++++++++++++++++++++++++++++++++  
// où placer myPID.SetTunings	 ??			 
                 myPID.SetTunings( Kp,  Ki,  Kd);  				 
                 //myPID.SetMode(MANUAL);
                 //myPID.SetTunings( Kp,  Ki,  Kd);             
                 // ------------------------------  fin entree  
                 // lancement du mouvement 
                 int n= 0;
                 long resc[nb];  // avant  : double
                 long resm[nb]; //  avant : double
                 long rest[nb];//long unsigned
                 bool calcule;
                 long date,date0;
                 date0=micros(); 
                 Commande=0;                    
                
                 //activation PID 
                 attend10();      
                 myPID.SetMode(AUTOMATIC);
                 while (n<nb) {
                        //----------------------------------------------------------
                  Mesure=MesurePosition();
                        date=micros()-date0;                   
                        calcule=myPID.Compute();              
                        if (calcule) {     
                        resm[n]=Mesure;
                        rest[n]=date;
                        //resc[n]=le_zero;    
                        resc[n]=Commande;                          
                        Fait_PWM(int(Commande/1000.));// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                
                        n++;                 
                     }
                  } // fin while n<nb
                  //myPID.SetMode(MANUAL);// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                  Fait_PWM(0); // arreter moteur
                 
                  Serial.print(F(" ; ; ; ; Correcteur: Kp= "));Serial.print(myPID.GetKp());
                  Serial.print(" Ki= ");Serial.print(myPID.GetKi());
                  Serial.print(" Kd=  ");Serial.println(myPID.GetKd()); 
                  Serial.print(F("; ; ; ;Consigne [deg] : "));Serial.println(Consigne/points_par_degre,1);// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                  Serial.println(F("date;Consigne;Mesure;Umoteur;Commande"));
                  Serial.println(F("[s];[deg];[pt];[V];[pt]"));
                  //Serial.print(0);Serial.print("; ");  Serial.print(0);Serial.print("; ");
                  //Serial.print(0);Serial.print("; ");//
                  //Serial.println(0);
                  n=0;
                  while (n<nb) {
                        Serial.print(double(rest[n])/1e6,3);Serial.print("; ");  Serial.print(Consigne/points_par_degre,2);Serial.print("; ");
                        Serial.print(resm[n]);Serial.print("; ");//
                        Serial.print((resc[n]*24.0)/255.0/1000.0,3); // la tension alim est 24V
                        Serial.print("; ");Serial.println(long(resc[n]/1000)); // la tension alim est 12V   
                        n++;
                  }// fin while n< nb
                  Serial.println();
                  Serial.println(F(" fini"));
                  //while(true){}
}
// -------------------------------------------------------------------
void Codeur()
{
      // Debut codeur              
                Serial.println(F("***************************** "));
                Serial.println(F("ERICC "));
                Serial.println(F("Mode de fonctionnement du codeur"));
                Serial.println(F("   Le rotor est deplace manuellement,"));
                Serial.println(F("   la position est donnee en points"));
                Serial.println(F("   (Entree pour demarrer et pour arreter)")); 
                // mode position
                ///30 mai debut
               // REG_TC0_BMR = TC_BMR_QDEN
                //            | TC_BMR_POSEN
               //             | TC_BMR_EDGPHA;  
                // Set everything going
               // REG_TC0_CCR0 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
              //  REG_TC0_CCR1 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
               // REG_TC0_CCR2 = TC_CCR_CLKEN | TC_CCR_SWTRG;
// 30mai fin
                libereMoteur();
                bool OK=false;              
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
                                
                          
                 // Serial.println(F(" Entree pour arreter"));
                 // si quelque chose sur port serie,le lire :
                 long positPt=MesurePosition();
                 Serial.print(positPt);Serial.println("  pts");
                 while (Serial.available() ==0) {                         
                       //----------------------------------------------------------
                      long iPos0 = MesurePosition();
                      if (abs(positPt - iPos0)>=50)
                            { int u_detect=analogRead(A0);
                              Serial.print(iPos0);Serial.print("  pts ;   fdc = ");Serial.print(u_detect);Serial.println("  pts");
                              positPt = iPos0;
                            attend10000();}
                              
                  ;};// fin while Serial       
                /* 
                  REG_TC0_BMR = TC_BMR_QDEN
                              | TC_BMR_SPEEDEN
                              | TC_BMR_EDGPHA;
            
                  REG_TC0_CCR0 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                  REG_TC0_CCR1 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                  REG_TC0_CCR2 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                  */
                  //while(true){}  // Rester dans boucle infinie
}

//-----------------------------------------------------------------------------
int choisirMenu()
{  
  Serial.println(F(""));
  Serial.println(F(" ********************************************"));
  Serial.println(F(" *      ERICC Asservissement de position    *"));
  Serial.println(F(" ********************************************"));
  Serial.println(F("                                         v1"));
  Serial.println(F(""));
  Serial.println(F("Choix :"));
  //Serial.println(F(" - Boucle Ouverte regime permanent   12V --->   1"));
  //Serial.println(F(" - Boucle Ouverte regime transitoire 12V --->   2"));
  Serial.println(F(" - Initialisation axe                    --->   0"));
  Serial.println(F(" - Boucle Fermee echelon de position     --->   1"));
  Serial.println(F(" - Mode de fonctionnement du codeur      --->   2"));
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


void attend_vraiment(int n=0){for (int x=0 ; x< n; x++){{for (int j=0 ; j< n; j++){;}}} } 
 // -------------------------------------------------------------------
void Initialisation_axe()
{
// faire la recherche du zero puis mettre compteur à 0
//Serial.println(F(" Mise a zero"));
// ************************************************************************
/*                // mode position

                REG_TC0_BMR = TC_BMR_QDEN
                            | TC_BMR_POSEN
                            | TC_BMR_EDGPHA;  
                // Set everything going
                REG_TC0_CCR0 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                REG_TC0_CCR1 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                REG_TC0_CCR2 = TC_CCR_CLKEN | TC_CCR_SWTRG;
                le_zero=  REG_TC0_CV0; //--------------------------------------------------->> 30 mai 2017
*/
 Serial.println(F("Initialisation de l axe : (Entree) "));
 Serial.println(F("***********************************"));
         while ((Serial.read() != '\n')){
            delay(400);   // attente 400ms
            }
         Serial.println(F("ATTENTION !! "));         
         delay(1000);   // attente 1000ms          
         trouveZero();
         faireZeroInit();
                
  ;}
//-----------------------------------------------------------------------
void trouveZero()
  {
  traverse(20);
  pos_fdc=MesurePosition(); 
  //Serial.print("pos 39 ");Serial.println(pos_fdc);
  traverse(15);
  pos_fdc=MesurePosition(); 
  //Serial.print("pos 39 ");Serial.println(pos_fdc);
  traverse(15);
  pos_fdc=MesurePosition(); 
  //Serial.print("pos 39 ");Serial.println(pos_fdc);
  }
//------------------------------------------------------------------------
void faireZeroInit()
  {
          Serial.println(F("Debut initialisation de l axe"));
          long date,date0;
           Consigne =MesurePosition() - pt_fdc ; //   
          //Serial.print(" posactuelle ");Serial.println(MesurePosition())  ;   
          // Serial.print(" Consigne pour zero ");Serial.println(Consigne)  ;   
           myPID.SetOutputLimits(-255000, 250000);/// x1000
           myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms   ******* 
           //++++++++++++++++++++++++++++++++++              
           //activation PID    
           posinit=MesurePosition();   
           myPID.SetMode(AUTOMATIC);
           myPID.SetTunings( 10, 5,  1);   //???????????????????????          
           // ------------------------------  fin entree  
           // lancement du mouvement 
           bool calcule;
           Commande=0; 
           //Serial.print("avant pos 0  ");Serial.println(posinit); 
           date0=millis(); 
           date=0;
           while( date < 800)
                  {       
                   Mesure=MesurePosition(); //-posinit;                 
                   date=millis()-date0;              
                   calcule=myPID.Compute();
                   if (calcule) 
                       {Fait_PWM(int(Commande/1000.));}
                  }
                  //Serial.print("comm ");Serial.println(Commande/1000);           
                  myPID.SetMode(MANUAL);
                  Fait_PWM(0); 
                  le_zero=MesurePosition(); ; 
                  //Serial.print("pos 0 ");Serial.println(le_zero);      
          

// ************************************************************************
                // mode position
/*                REG_TC0_BMR = TC_BMR_QDEN
                            | TC_BMR_POSEN
                            | TC_BMR_EDGPHA;  
                // Set everything going
                REG_TC0_CCR0 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                REG_TC0_CCR1 = TC_CCR_CLKEN | TC_CCR_SWTRG;  
                REG_TC0_CCR2 = TC_CCR_CLKEN | TC_CCR_SWTRG;
            REG_TC0_CCR0 = 5;
*/
            attend_vraiment(100);
            posinit=MesurePosition(); 

           attend_vraiment(100);  
           Serial.println(F("Fin initialisation de l axe"));  
           Serial.println(F(" **************************"));         
  }
//------------------------------------------------------------------------  
void traverse(int lePwm)
  {
 //   utiliser  int u_detect=analogRead(A0);
        if ( analogRead(A0) <600)
              {digitalWrite(PIN_DIR1,HIGH);digitalWrite(PIN_DIR2,LOW);
              while ( analogRead(A0) <600)
              {analogWrite(PIN_COMMANDE, lePwm);  
              }
              analogWrite(PIN_COMMANDE,0);
              }
        else
              {digitalWrite(PIN_DIR1,LOW);digitalWrite(PIN_DIR2,HIGH);
              while ( analogRead(A0) >600)
              {analogWrite(PIN_COMMANDE, lePwm);  
              }
              analogWrite(PIN_COMMANDE,0);}; 
         attend_vraiment(50);
  }      
// ------------------------------------------------------
//------------------------------------------------------------------------------
void libereMoteur()  // liberer le moteur
    { analogWrite(PIN_COMMANDE, 0);
    digitalWrite(PIN_DIR1,HIGH);
    digitalWrite(PIN_DIR2,HIGH);
     }
//-----------------------------------------------------------------------------         
//-----------------------------------------------------------------------------

void Fait_PWM(int y)  // commande moteur
    { analogWrite(PIN_COMMANDE, 0);
      if (y <0) {   digitalWrite(PIN_DIR1,LOW);digitalWrite(PIN_DIR2,LOW);attend();
                    digitalWrite(PIN_DIR1,LOW);digitalWrite(PIN_DIR2,HIGH);y=-y;}
      else{digitalWrite(PIN_DIR1,HIGH);;digitalWrite(PIN_DIR2,LOW);}
    analogWrite(PIN_COMMANDE, y);
     }

     
void attend(){;}   

void attend10(){
  for (int i=0; i <= 20000; i++){
  ;} 
} 
void attend10000(){
  for (int i=0; i <= 20000; i++){
    int k=0;
    for (int i=0; i <= 20000; i++){k=k+1;
  ;}
  ;} 
}

long MesurePosition()
{
 //int iIndexCount = REG_TC0_CV1;  // Don't need this, but manual notes its available  
//int iSpeedPPP = REG_TC0_RA0;    // This is what we're really after (speed in Pulses Per sample Period)  

long positPt=REG_TC0_CV0-le_zero; //---------------------------------------------------------------------------<< 30 mai 2017
return positPt;                       //----------------------------------------------------------                 
}


