/**************************************************************
 * ROBOT ERICC3                                               *
 * Axe poignet                                                *
 * tests  asservissement de position                          *
 * Octobre 2017 v3 mise en degres                             *
***************************************************************/
//
//-------------------------------------------------------------------------------
#include <PID_v1.h>
#include <Wire.h>
//Moteur :
#define PIN_DIR_D 12   // direction moteur poignet A
#define PIN_COMMANDE_D 3 // power du moteur poignet A  (c'est une PWM) 
#define PIN_FDC4 40 // signal fin de course poignet
// shield moteur M+  = le blanc ; M- : le noir 


// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
//   avoid using pins with LEDs attached

// ************************************************************************************
const int SNS_B=A1;  // pin mesure courant moteur pince
const int SNS_A=A0;  // pin mesure courant moteur poignet
const int nb=400;  // nombre de points de mesure 150
const int periode_echant=5; // periode echantillonnage

/*
L'angle du fdc est 38 degres soit 273.14815*38 points.
Si la position au demarrage est < 38 alors fdc4 =1 sinon fdc4 =0
 */
const float points_par_degre=273.148148;
const long int pt_fdc=int(points_par_degre*37);


float duree=600000;
//
//
double Consigne, Mesure, Commande;  // grandeurs en points

//Valeur par defaut du PID
double ech,Kp=0.0, Ki=0, Kd=0;
PID myPID(&Mesure, &Commande, &Consigne, Kp, Ki, Kd, DIRECT);// ancienne position
//long unsigned date0;
long posinit,pos39;

void setup()
{
pinMode(PIN_DIR_D, OUTPUT); 
pinMode(PIN_COMMANDE_D, OUTPUT);      
  // si quelque chose sur port série,le lire :
//bool OK=false;
// initialisation port série:
Serial.begin(115200);
  Wire.begin();        // joindre le bus i2c (adresse est optionnelle pour un maître)



 //send n seed
  Wire.beginTransmission(2); 
  Wire.write(byte(0));               
  Wire.endTransmission();  
Serial.println(F("ERICC 3 axe poignet "));      
}

void loop()
{
  int fdc;
  long old_posit;
  //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  int choix=choisirMenu();
    switch (choix) {
    case 0:  // rien    
         Serial.println(" ");       
         break;         
 
    case 1:  // etalonnage potentiometre
         Serial.println(F(" "));
         Serial.println(F("Recherche du zero et mise en position initiale (Entree) "));
         while ((Serial.read() != '\n')){
            delay(400);   // attente 400ms
            }
         Serial.println(F("ATTENTION !! "));         
         delay(1000);   // attente 1000ms          
         trouveZero();
         faireZeroInit();
         break;      
    
    case 2:
          Serial.println(recupPosition());
          // cas direction BF echelon position: 
          Serial.println(F(" "));
          Serial.println(F(""));
          Serial.println(F("        Asservissement de position  :"));
          Serial.println(F(""));
          choix_conditions_echelon();
          Fait_echelon();
          break;
    case 3:
          Serial.println(F(" "));
          Serial.println(F(""));
          Serial.println(F("        Etude detecteur  :"));
          Serial.println(F(""));
          Serial.println(F("Entree pour finir"));
          Serial.println(F(""));          
          Serial.println(F("posit[points]; angle relatif[deg] ; etat detect[0/1] "));
          
          posinit=recupPosition();
          old_posit=posinit;
          while ((Serial.read() != '\n'))
                {  
                int fdc=digitalRead(PIN_FDC4);
                long posit=recupPosition()-posinit;
                if (posit != old_posit )
                     {
                           Serial.print(posit); Serial.print(" ; ");Serial.print(posit/273.148148); Serial.print(" ; ");
                           Serial.println(fdc);
                           old_posit=posit;
                     }
                delay(20);
                }   
          break;
          
            /*    default:
                      while(true){} //bloque le programme;
                      break;
            */          
  }  // fin switch choix
}
//**************************************************

//------------------------------------------------------------------------
int choisirMenu()
    {  
    Serial.println(F(""));
    Serial.println(F("      ********************************************"));
    //Serial.println(F("      *                                          *"));
    Serial.println(F("      *            ROBOT ERICC 3                 *"));
    Serial.println(F("      *            Axe de poignet                *"));
   // Serial.println("      *                                          *"));
    Serial.println(F("      ********************************************"));
    Serial.println(F("                                              v3"));
    Serial.println(F(""));
    Serial.println(F("   Choix :"));
    //Serial.println(F("      - Sortir                                --->   0")); 
    Serial.println(F("      - Mise au zero de l'axe                  --->   1"));
    Serial.println(F("      - Asservissement en position ,echelon    --->   2"));
    Serial.println(F("      - Etude detecteur                        --->   3"));   
    Serial.println(F("      - Asservissement en position ,trapeze V  --->   4"));
    Serial.println(F("              (.... et Entree)"));
   
     bool OK=false;
     // MENU 
          int choix;
          while(OK== false){
            // si quelque chose sur port serie,le lire :  
                while (Serial.available() > 0) {                
                      // recherche du prochain entier sur le port serie:
                       choix = Serial.parseInt();         
                      // recherche du caractere nouvelle ligne pour terminer                        
                      if (Serial.read() == '\n') {
                              choix = constrain(choix, 1, 3);    //limiter choix  
                              OK=true;
                              } // fin if Serial                 
                 };// fin while Serial.available
           }// fin while OK false
       return choix;
     }  
//-----------------------------------------------------------------------

// fonctions d'attente
void attend(){for (int x=0 ; x< 50; x++){;}} 
void attend_vraiment(int n=0){for (int x=0 ; x< n; x++){{for (int j=0 ; j< n; j++){;}}} }     
// -------------------------------------------------------------------
void choix_conditions_echelon()
{
 // choix correcteur--------------------------------------------------------------------------                
                Serial.println(F("Correction : entrer Kp, Ki et Kd flottants positifs separes par des virgules"));
                Serial.println(F("Kp [10 .. 200] Ki[0.. 50]  Kd[0.. 50]"));
               
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
                        // recherche du caractère nouvelle ligne pour terminer
                    
                        if (Serial.read() == '\n') {
                          iKp = constrain(iKp, 10, 200);    //limiter Kp
                          iKi =constrain(iKi, 0, 50);    // limiter Ki 
                          iKd =constrain(iKd, 0, 50);    // limiter Kd
                
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
                  Serial.println(F("  Entrer une consigne de position en degres  [-90 ..90]"));//[-24570 ..24570]
                OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {               
                        // recherche du prochain entier sur le port serie:
                        float iech = Serial.parseFloat();         
                        // recherche du caractère nouvelle ligne pour terminer                  
                        if (Serial.read() == '\n') {
                          // constraint la valeur dans un intervalle
                          ech = constrain(iech,-90, 90);    //limiter Kp              
                          // affiche :
                          Serial.print(F("  Consigne= "));
                          Serial.print(ech);Serial.println(F("  [degres]"));
                          OK=true;
                        } // fin if Serial
                     Serial.println("--------------------"); 

                   };// fin while Serial.available
                 }// fin while OK false               
                 //fin choix echelon
                 Consigne = (points_par_degre*ech); 
}
// -------------------------------------------------------------------
void choix_conditions_trapeze()
{
 // choix correcteur--------------------------------------------------------------------------                
                Serial.println(F("Correction : entrer Kp, Ki et Kd flottants positifs separes par des virgules"));
                Serial.println(F("Kp [10 .. 200] Ki[0.. 50]  Kd[0.. 50]"));
               
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
                        // recherche du caractère nouvelle ligne pour terminer
                    
                        if (Serial.read() == '\n') {
                          iKp = constrain(iKp, 10, 200);    //limiter Kp
                          iKi =constrain(iKi, 0, 50);    // limiter Ki 
                          iKd =constrain(iKd, 0, 50);    // limiter Kd
                
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
                Serial.println("Entrer trapeze(points), vitesse(points/ms) ,temps montee(ms),horizon temporel separes par des virgules");
Serial.println(" trapeze[0..1000000L] vitesse[0..15] temps[50..300] horizon temporel[0..2000]");
while(OK== false){  
while (Serial.available() > 0) {

    // recherche du prochain entier sur le port série:
    float iLTot = Serial.parseFloat();
    // encore:
    float iV0 = Serial.parseFloat();
    // encore:
    float idt0 = Serial.parseFloat();
        // encore:
    float ihorizon = Serial.parseFloat();
    // recherche du caractère nouvelle ligne pour terminer

    if (Serial.read() == '\n') {
      // constrain the values to 0 - 255 et inverse
      LTot = constrain(iLTot, 0, 1000000L);    //limiter deplacement
      V0 = constrain(iV0, 0, 15);    //limiter vitess
      dt0 = constrain(idt0, 50,300);    //limiter temps montée
      horizon = constrain(ihorizon, 0,2000);    //limiter temps montée
      // affiche :
      Serial.print("Trapèze= ");
      Serial.println(LTot);
      Serial.print("Vitesse= ");
      Serial.println(V0);
      Serial.print("temps montee= ");
      Serial.println(dt0);
      Serial.print("horizon temporel= ");
      Serial.println(horizon);
      OK=true;
 
 }
 Serial.println("--------------------"); 
} 
}

}
//-----------------------------------------------------------------------
void trouveZero()
  {
  traverse(20);
  pos39=recupPosition();
  //Serial.print("pos 39 ");Serial.println(pos39);
  traverse(15);
  pos39=recupPosition();
  //Serial.print("pos 39 ");Serial.println(pos39);
  traverse(15);
  pos39=recupPosition();
  //Serial.print("pos 39 ");Serial.println(pos39);
  }
//------------------------------------------------------------------------
void faireZeroInit()
  {
          Serial.println(F(" Recherche et mise au zero"));
          long date,date0;
           Consigne = -pt_fdc; //         
           myPID.SetOutputLimits(-255000, 255000);/// x1000
           myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms   ******* 
           //++++++++++++++++++++++++++++++++++              
           //activation PID    
           posinit=recupPosition();   
           myPID.SetMode(AUTOMATIC);
           myPID.SetTunings( 60, 5,  5);   //???????????????????????          
           // ------------------------------  fin entree  
           // lancement du mouvement 
           bool calcule;
           Commande=0; 
           date0=millis(); 
           date=0;
           while( date < 800)
                  {       
                   Mesure=recupPosition()-posinit;                 
                   date=millis()-date0;              
                   calcule=myPID.Compute();
                   if (calcule) 
                       {Fait_PWM(int(Commande/1000.));}
                  }
                  //Serial.print("comm ");Serial.println(Commande/1000);           
                  myPID.SetMode(MANUAL);
                  Fait_PWM(0); 
                  posinit=recupPosition(); 
                  //Serial.print("pos 0 ");Serial.println(posinit);      
          
          attend_vraiment(100);             
  }
//------------------------------------------------------------------------  
void traverse(int lePwm)
  {
        if ( digitalRead(PIN_FDC4) ==1)
              {digitalWrite(PIN_DIR_D,HIGH);
              while ( digitalRead(PIN_FDC4) ==1)
              {analogWrite(PIN_COMMANDE_D, lePwm);  
              }
              analogWrite(PIN_COMMANDE_D,0);
              }
        else
              {digitalWrite(PIN_DIR_D,LOW);
              while ( digitalRead(PIN_FDC4) ==0)
              {analogWrite(PIN_COMMANDE_D, lePwm);  
              }
              analogWrite(PIN_COMMANDE_D,0);}; 
        attend_vraiment(50);
  }      
// ------------------------------------------------------
void Fait_echelon()
{
                 myPID.SetOutputLimits(-255000, 255000);/// x1000
                 myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms ******* 
                 //++++++++++++++++++++++++++++++++++              
                 //activation PID       
                 myPID.SetMode(AUTOMATIC);
                 myPID.SetTunings( Kp,  Ki,  Kd);             
                 // ------------------------------  fin entree  
                 // lancement du mouvement 
                 int itest=0;               
                 int n= 0;
                 bool encore=true;
                 int resu[nb];  // avant  : double
                 double resv[nb]; //  avant : double
                 double Mesure_m1;
                 double rest[nb];//long unsigned int
                 int courant;
                 //unsigned int resi[nb];
                 bool calcule;
                 double date,date0;
                 double date_m1;
                 long posit,posit_m1;
                 date0=micros(); 
                 Commande=0;                    
                 posinit=recupPosition();
                 //Serial.print(" ***  ");Serial.println(posinit);
                 Mesure=0;
                 while (n<nb) {
                    //dt=micros(); // 0 us 
                    //courant=analogRead(SNS_A);//lecture courant ligne 200 us      
                    Mesure=recupPosition()-posinit;                 
                    date=micros()-date0;              
                    calcule=myPID.Compute();
                                 
                    if (calcule) { 
                        resv[n]=Mesure;
                        rest[n]=date;
                        resu[n]=int(Commande*12/255.);//Umot en mV
                        //resi[n]=courant;       
                        Fait_PWM(int(Commande/1000.));              
                        n++;                 
                        }
                itest++;
               } // fin while n<nb
                  //myPID.SetMode(MANUAL);
                  Fait_PWM(0);
                                  
                   Serial.print(" Correcteur: Kp= ");Serial.print(myPID.GetKp());
                   Serial.print(" Ki= ");Serial.print(myPID.GetKi());
                   Serial.print(" Kd=  ");Serial.println(myPID.GetKd()); 
                   Serial.print(F("; ; ; ; ;Consigne [pt] : "));Serial.println(Consigne);
                   // +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++             
                   Serial.println(F("date;Consigne;Mesure;Commande"));
                   Serial.println(F("[s];[pt];[pt];[mV]"));
                   Serial.print("0");Serial.print("; ");  Serial.print(0 );Serial.print("; ");
                   Serial.print("0");Serial.print("; ");//
                   Serial.print("0");Serial.println("; ");
                   n=0;
                   while (n<nb) {
                        Serial.print(rest[n]/1.0e6,3);Serial.print("; ");  Serial.print(ech,2);Serial.print("; ");
                        Serial.print(resv[n]/points_par_degre,2);,0);Serial.print("; ");//
                        Serial.print(resu[n]/1000.);Serial.println("; ");
                        n++;
                   }// fin while n< nb
                   Serial.println();
                   Serial.println(F(" fini"));
                    // Serial.print(itest); Serial.println(F(" ++++++++++++ "));
                   analogWrite(PIN_COMMANDE_D, 0);
                   trouveZero();
                   faireZeroInit();
}  
//**************************************************
 // récupérer position 
 long recupPosition()
 {
      byte b[4];
      int i=0; 
      Wire.requestFrom(2, 4);    // lecture de 4 octets (bytes) depuis l'esclave #2
      while(Wire.available())    // l'esclave pourrait envoyer moins de données qu'attendu
          {
            b[i] = Wire.read();    // Reception de l'octet (byte) comme caractère
            i++;
            //    Serial.print(b[i]);
          }
        return   recompose(b[3],b[2],b[1],b[0])/4;// /4 pour enlever quadrature !!!!!!!!!!!!!!!!!!!!!!!!
    }
//------------------------------------------------------------------------
long recompose(byte b3,byte b2,byte b1,byte b0)
{
       long c;
       if (b3 >>7 == 0)
          {
            // positif
            c=0L+b0 +(0L+ b1 <<8 )+(0L+ b2 << 16) + (0L+b3 << 24);
          }
       else 
          {
               b3=~b3 ; 
               b2=~b2; 
               b1=~b1 ;
               b0=~b0 ;
            c=-1L-b0 -(0L+ b1 <<8 )-(0L+ b2 << 16) - (0L+b3 << 24);
          }
  return c;
  }
// -------------------------------------------------------------------
void Fait_PWM(int y)  // commande moteur
    { if (y <0) { analogWrite(PIN_COMMANDE_D, 0);attend();digitalWrite(PIN_DIR_D,LOW);}
      else{analogWrite(PIN_COMMANDE_D, 0);attend();digitalWrite(PIN_DIR_D,HIGH);}
      attend();
      analogWrite(PIN_COMMANDE_D, abs(y));
    } 
//-----------------------------------------------------------
 long Trapeze(long Lt,int VO, int dt0,long t)  //
 {
  if (Lt>=V0*dt0)  //déplacement total suffisant
   {
     int dtv= int(1.0*Lt/V0)-dt0;
     if (t< dt0)               //phase 1
       {return  long(V0*t*t/dt0/2.);
         }
        else
         {
           if (t<dt0+dtv)      // phase 2
           {return long(V0*(t-dt0/2.));
             }
            else{
              if(t<2*dt0+dtv)  //phase3
              {return long(V0*(dt0+dtv-pow(dtv+2*dt0-t,2.)/2/dt0));
                }
                else return Lt;//phase4
              } 
     } 
   }
   else  // déplacement total court
    {  float dt1=sqrt(1.0*Lt*dt0/V0) ;
      float V1=sqrt(1.0*Lt*V0/dt0);
    if (t<dt1)
      {return long(V0*t*t/2./dt0);
      }
      else
     { 
      if(t<= 2*dt1)
        {return long(V1*dt1-V0*pow(t-2.*dt1,2.)/2./dt0);
         } 
         else return Lt;
         }
      }  
 } 