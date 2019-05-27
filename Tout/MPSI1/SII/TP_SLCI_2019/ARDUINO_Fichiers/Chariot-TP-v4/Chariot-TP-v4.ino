/**************************************************************
 * chariot filoguide                                          *
 * Novembre 2018                                               *
 * ajout asservissement de vitesse                            *
***************************************************************/
/* deux possibilites : 
      + etalonnage potentiometre
      + direction BF echelon avec choix PID

   ********************************************
   *                                          *
   *            CHARIOT FILOGUIDE             *
   *                                          *
   *                T.P. N  1                 *
   ********************************************
                                           v 4
Choix :
    - Etalonnage potentiometre             --->   1
    - Asservissement de position direction --->   2
    - Asservissement de position avance    --->   3
    - Asservissement de vitesse avance     --->   4
    - Commande en boucle ouverte avance    --->   5 



/*
  Lecture de Kp, Ki et Kd
separes par une virgule et contraints a rester dans un intervalle precis
L'echelon est choisi entre 0 et 60 .
*/

//-------------------------------------------------------------------------------
#include <PID_v1.h>
#include <Wire.h>


// *********** chaine avance ***********************************************
//
// Moteur avance
#define PIN_DIRa 13   // direction moteur direction A
#define PIN_COMMANDEa 11 // power du moteur A  (c'est une PWM)
const int SNS_B=A1;  // pin mesure courant moteur avance
// *********  chaine direction  ***********************************
//
// pour le moteur et le potentiometre
//Potentiometre : Alimentation vert =5V,jaune=Gnd
//                Mesure bleu 
#define  PIN_MESURE 7   //mesure du potentiometre de direction
//Moteur direction  :
#define PIN_DIR 12   // direction moteur direction A
#define PIN_COMMANDE 3 // power du moteur A  (c'est une PWM)
// shield moteur M+  = le blanc ; M- : le noir 
//  apres etalonnage du potentiometre:
const float zero_mes = 720;
const float inc_deg = 3.0056;
//
const byte periodeEchantDir=8;
const byte periodeEchantAvPos=5;
const byte periodeEchantAvVit=2;

const int nbDir =200;// nb points asservissement direction en position 
const int nbAvPos =200;// nb points asservissement avance en position
const int nbAvVit =200;// nb points asservissement avance en vitesse
const int duree = 4000; // duree 4 s de la boucle ouvert en avance

// ********** acquisition  ***************************************
byte nb;  // nombre de points de mesure (150 .. 200)
//byte periode_echant; // periode echantillonnage enn ms (2..10)
long unsigned date,date0;

// **********  PID  **********************************************
double Kp , Ki , Kd ;
double Mesure, Commande, Consigne;
PID myPID(&Mesure, &Commande, &Consigne, Kp, Ki, Kd, DIRECT);// ancienne position

void setup()
  {
  pinMode(PIN_DIR, OUTPUT); 
  pinMode(PIN_COMMANDE, OUTPUT);
  pinMode(PIN_DIRa, OUTPUT); 
  pinMode(PIN_COMMANDEa, OUTPUT);
  Serial.begin(115200); // initialisation port serie, choix debit
  Wire.begin();        // joindre le bus i2c (adresse est optionnelle pour un maître)
  }

void loop()
  {
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   byte choix=choisirMenu();
   Serial.println();
   switch (choix) {
    case 0: { // rien    
       Serial.println();
    }       
       break;         
 
    case 1:{  // etalonnage potentiometre
            Fait_etalonnage();
           }
        break;      
	  
    case 2:{
            // cas direction BF echelon position: 
            Fait_echelon_pos_dir(); 
            }        
       break;
       //fin cas  dir echelon  cas 2
//**************************************************************************************       
       case 3: { // asservissement de position avance
            Fait_echelon_pos_avance();
                }
        break;  
  
//**************************************************************************************       
       case 4: { // asservissement de vitesse avance
            Fait_echelon_vitesse_avance();
                }
        break;  
  
//**************************************************************************************       
       case 5: { // Commande en boucle ouverte avance
                Fait_BO_avance();}
        break;  
    } // fin switch           	   
   
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  Serial.println();
  Serial.println(F(" Entree pour revenir au menu"));
  while((Serial.read() == '\n')){}  // boucle infinie  
  } //fin void loop

//------------------------------------------------------------------------
  int choisirMenu()
  {  

  Serial.println(F("   ******************************************"));
  Serial.println(F("   *           CHARIOT FILOGUIDE            *"));
  Serial.println(F("   ******************************************"));
  Serial.println(F("                                     v4"));
  Serial.println(F("Choix :"));
  Serial.println(F("  - Etalonnage potentiometre              ---> 1"));
  Serial.println(F("  - Asservissement en position  direction ---> 2"));
  Serial.println(F("  - Asservissement en position avance     ---> 3"));
  Serial.println(F("  - Asservissement en vitesse avance      ---> 4"));
  Serial.println(F("  - Commande en boucle ouverte avance     ---> 5"));
  Serial.println();
  
   //-------------------------Choix menu -----------------------------
   byte choix=LireEntier(" choix et entree ",0,5);
   return choix;
  }      
// -------------------------------------------------------------------
void Fait_etalonnage()
{
  /*
   On déplace la fourche de direction à la main , on peut avoir pour une position imposee et lue en degre, 
   la valeur de la tension de mesure du potentiometre et la valeur brute en sortie du C.A.N. 10 bits  
   */
  Serial.println(F(" "));
        Serial.println(F("Etalonnage du potentiometre (Entree pour sortir)"));
        int ancienAngle=0;
        int mesureAngle;
        while ((Serial.read() != '\n')){
          mesureAngle = analogRead(PIN_MESURE);    // lecture PIN_MES:
          if (abs(mesureAngle-ancienAngle)>5)
              {
                Serial.print(F("mesure= "));Serial.print(mesureAngle);Serial.print(F(" pt  ")); 
                Serial.print(mesureAngle*5/1023.0,2);Serial.println(F(" V"));// imprime sur la sortie serie:
                ancienAngle=mesureAngle;
              }
          delay(1000);   // attente 400ms
          } 
}

// -------------------------------------------------------------------
void Fait_echelon_pos_dir()
{       
double ech;
nb=nbDir;  // nombre de points de mesure 150
       // cas direction BF echelon position: 
                Serial.println();
                Serial.println();
                Serial.println(F("        Asservissement de position de la direction:"));
                Serial.println();
                Serial.println(F("Correcteur:"));
                // choix correcteur--------------------------------------------------------------------------                
                Kp=LireFlottant("Kp flottant [0..20] ? ",0,20);
                Ki=LireFlottant("Ki flottant [0..5] ? ",0,5);
                Kd=LireFlottant("Kd flottant [0..5] ? ",0,5);                
                          Serial.println(F("--------------------"));
                          Serial.print(F("  Kp= "));
                          Serial.print(Kp);
                          Serial.print(F("   "));
                          Serial.print(F("Ki= "));
                          Serial.print(Ki);
                          Serial.print(F("   "));
                          Serial.print(F("Kd= "));
                          Serial.println(Kd);
                 // choix echelon---------------------------------------------------------------------
                int pos_init;
                float pos_init_deg;

                ech=LireEntier(F("  Echelon:  Entrer un echelon compatible  avec une position finale dans [-60 ..60]"),-60-pos_init_deg ,60-pos_init_deg );
                pos_init=analogRead(PIN_MESURE)-zero_mes;
                pos_init_deg=pos_init/inc_deg;
                Serial.print(F("Position initiale:  "));Serial.print(pos_init_deg,2);Serial.println(F(" degres"));    
                Serial.println();                
                 // petite attente:
                 for (int y=0; y<10;y++){ 
                   for (int x=0 ; x< 30000; x++){if (x % 15000==0){      Serial.print("*");} }
                   };
                 Serial.println();  
                
                 //initialisation des variables
                 Mesure=pos_init;
                 Consigne = int(ech*inc_deg)+pos_init; //         
                 myPID.SetOutputLimits(-255, 255);
                 myPID.SetSampleTime(periodeEchantDir);  // Periode d'echantillonnage en ms   ******* 
                     
                
                 //++++++++++++++++++++++++++++++++++              
                 //activation PID       
                 myPID.SetMode(AUTOMATIC);
                 myPID.SetTunings( Kp,  Ki,  Kd);             
                 // ------------------------------  fin entree  
                 // lancement du mouvement 
                 date0=millis();                
                 byte n= 0;
                 bool  encore=true;
                 int resc[nb];  // avant  : double
                 int resm[nb]; //  avant : double
                 unsigned int rest[nb];
                 unsigned int resi[nb];
                 bool calcule;
                 Commande=0;
                 Mesure=0;
                 while (n<nb) {
                    date=millis()-date0;
                    calcule=myPID.Compute();           
                    if (calcule) {        
                        resc[n]=int(Commande);  
                        resm[n]=int(Mesure);
                        rest[n]=date;
                        Mesure = analogRead(PIN_MESURE)-zero_mes;
                        resi[n]=analogRead(A0);//lecture courant        
                        //Serial.println(n);
                        Fait_PWM(int(Commande));
                        n++;
                        }
                  } // fin while n<nb
                  myPID.SetMode(MANUAL);
                  Commande=0;
                  Fait_PWM(0);
                 
                  Serial.print(F("Kp "));Serial.println(myPID.GetKp());
                  Serial.print(F("Ki "));Serial.println(myPID.GetKi());
                  Serial.print(F("Kd "));Serial.println(myPID.GetKd()); 
                  Serial.print(F("Mesure initiale [pt]: "));Serial.println(pos_init);// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                  Serial.print(F("Consigne [pt]: "));Serial.println(Consigne-pos_init);// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                 Serial.println(F("date;Consigne;Sortie;Im_Cons;Mesure;Commande;Courant"));
                 Serial.println(F("[ms];[degre];[degre];[pt];[pt];[pt];[mA]"));
                  n=0;
                  while (n<nb) {
                      Serial.print(rest[n]);Serial.print(F(";"));
                      Serial.print((Consigne-pos_init)/inc_deg);Serial.print(F(";"));
                      Serial.print((resm[n]-pos_init)/inc_deg);Serial.print(F(";"));
                      Serial.print(Consigne-pos_init,0);Serial.print(F(";"));
                      Serial.print(resm[n]-pos_init);Serial.print(F(";"));
                      Serial.print(resc[n]);Serial.print(F(";"));Serial.println(resi[n]*10/(3.3*1.023),0);
                      n++;
                    }// fin while n< nb
                 Serial.println();
                 Serial.println(F(" Entree pour retour au menu"));
                 Serial.println();           
 //                myPID.SetMode(MANUAL); 
                 Fait_PWM(0);
    } 

//--------------------------------------------------------------------
//--------------------------------------------------------------------
void Fait_echelon_pos_avance()
{
    // ********** caracteristiques acquisition  ***************************************
    nb=nbAvPos;  // nombre de points de mesure 150
    int unsigned ech;
    
    Serial.println();
    Serial.println(F("Asservissement de position d'avance:"));
    ech=LireFlottant(F("Entrer echelon(points) [0..10000]"),0,10000);
    //-----------------------------------------------------
    
    Serial.println(F("Correcteur : "));
     // choix correcteur--------------------------------------------------------------------------                
      Kp=LireFlottant(F("Kp flottant [0..2] ? "),0,2);
      Ki=LireFlottant(F("Ki flottant [0..1] ? "),0,1);
      Kd=LireFlottant(F("Kd flottant [0..2] ? "),0,2);
                      
    Serial.println(F("--------------------"));
    //  petite attente  
    for (int y=0; y<10;y++){ 
    for (int x=0 ; x< 30000; x++){if (x % 15000==0){      Serial.print("*");} }};
    Serial.println();  
        
        //  *************************************************************************************               
                     //initialisation des variables
        //  **************************************************************************    
      myPID.SetOutputLimits(-255, 255);
      myPID.SetSampleTime(periodeEchantAvPos);  // Période d'échantillonnage en ms   ******* 
    
      Consigne = ech;
      Commande = 0; 
      Mesure=0; 
      
      //Démarrage PID
      myPID.SetMode(AUTOMATIC);
      myPID.SetTunings( Kp,  Ki,  Kd);   
    
    long posit;
    long posinit;
    unsigned int courant;
    // Tableaux stockage acquisition
    int resc[nb];  //  commande
    int resm[nb]; //  mesure
    //unsigned int resi[nb];// courant
    unsigned long rest[nb]; // temps
 
     bool calcule;
     // lancement du mouvement 
      date0=millis();
      posinit=recupPosition();   
      Commande=0; 
      Mesure=0;
      byte n= 0;
      // Pilotage et acquisition
      while (n<nb) {
              date=millis()-date0;
              // --------------------------------------------------------------------------
              //posit = recupPosition()-pos0;
              //posit = 0.8*recupPosition_v(date);           
              //---------------------------------------------------------------------------  
              calcule=myPID.Compute();           
              if (calcule) {                                                 
                    rest[n]=long(date);   
                    resc[n]=int(Commande); 
                    resm[n]=int(Mesure);
                    //resi[n]=analogRead(A1);
                    Mesure = recupPosition()-posinit;
                    n++;
                    Fait_PWMa(Commande);
                    }     
        } // fin while n<nb
        // Arret PID
        myPID.SetMode(MANUAL);
        Commande=0;
        Fait_PWMa(0); 
    
        // les resultats:
        //--------------- En tete:
        Serial.println(F("Correcteur: "));
        Serial.print(F("  Kp "));Serial.println(myPID.GetKp());
        Serial.print(F("  Ki "));Serial.println(myPID.GetKi());
        Serial.print(F("  Kd "));Serial.println(myPID.GetKd()); 
        //Serial.println(" date, Consigne, Mesure, Commande, Courant");
        Serial.println(F(" date;Consigne;Mesure;Commande"));
        Serial.println(F("[ms];[pt];[pt];[pt]"));
        Serial.print(0);Serial.print(F(";"));
        Serial.print(0);Serial.print(F(";"));
        Serial.print(0);Serial.print(F(";"));
        Serial.print(0);//Serial.print(F(";"));
        //Serial.print(0);
        Serial.println();
        n=0;
        while (n<nb) {
             Serial.print(rest[n]);Serial.print(F(";"));
             Serial.print(Consigne,0);Serial.print(F(";"));
             Serial.print(resm[n]);Serial.print(F(";"));
             //Serial.print(Consigne-resm[n],0);Serial.print(F(";"));
             Serial.print(resc[n]);
             Serial.print(F(";"));
             //Serial.print(int(resi[n]*10.0/(3.3*1.023)));// arduino motorshield
             Serial.println();
            n++;
            }// fin while n< nb
        Serial.println();
 }

 //-------ASSERVISSEMENT DE VITESSE CONSIGNE ECHELON ----------------------
//
void Fait_echelon_vitesse_avance()
  {
    /*
     * la vitesse maximum en B.O. est environ 27 pt par ms sous 9V. 
     * Donc si Te=2, la variation de mesure maximum est de 54 pt sur une période
     *  entrée de la consigne en pt  [0..100]
     * entrée de Kp, Ki, Kd   [0..10]
     * 
    */  
//********************************************************    
    nb=nbAvVit;  // nombre de points de mesure 150
//    byte periode_echant=2; // periode echantillonnage
//********************************************************    
    Serial.println();
    Serial.println();
    Serial.println(F("Asservissement de vitesse d'avance : echelon :"));
    Serial.println();
    Consigne=LireEntier(F("Entrer consigne de vitesse (points) [0..200]"),0,200);
    //-----------------------------------------------------    
    Serial.println(F("Correcteur :"));
     // choix correcteur--------------------------------------                
      Kp=LireFlottant(F(" Kp flottant [0..40] ? "),0,40);
      Ki=LireFlottant(F(" Ki flottant  [0..10] ? "),0,10);
      Kd=LireFlottant(F(" Kd flottant [0..5] ? "),0,5);
                      
    Serial.println(F("--------------------"));
    //  petite attente  
    for (int y=0; y<10;y++){ 
    for (int x=0 ; x< 30000; x++){if (x % 15000==0){      Serial.print(F("*"));} }};
    Serial.println();  
          
    //  *************************************************************************************               
                 //initialisation des variables
    //  **************************************************************************    
    myPID.SetOutputLimits(-255, 255);
    myPID.SetSampleTime(periodeEchantAvVit);  // Periode d'echantillonnage en ms   *******                                  

    //Commande=0; 
    //Mesure=0;   
    myPID.SetMode(AUTOMATIC);
    myPID.SetTunings( Kp,  Ki,  Kd);             
    // ------------------------------  fin entree  
    // initialisations: 
    // Tableaux stockage acquisition            
    int resc[nb];  // avant  : double
    int resm[nb]; //  avant : double
    unsigned long rest[nb]; 

    long int  Position,pos0;
    long int dernierePosition;// une mesure de position alors qu'on veut une vitesse
    unsigned long int derniereDate=0L;
    
     bool calcule;
    // lancement mouvement
    date0=micros();
    pos0=recupPosition();
    dernierePosition=0;
    Commande=0; 
    Mesure=0;
    // Pilotage et acquisition
    byte n= 0; 
    while (n<nb) {
          date=micros()-date0;
          // --------------------------------------------------------------------------
          //Position=recupPosition()-pos0;
           Position = 0.8*recupPosition_v(date);           
          //---------------------------------------------------------------------------  
           calcule=myPID.Compute();           
           if (calcule) { 
                rest[n]=long(date);   
                resc[n]=int(Commande); 
                resm[n]=Mesure;
                Mesure=int((Position-dernierePosition)*periodeEchantAvVit*1000./(date-derniereDate)); //
                //cette mesure sert a la prochaine evaluation de la commande              
                n++;
                dernierePosition=Position;
                derniereDate=date;
                Fait_PWMa(Commande);
                }
    } // fin while n<nb
    // Arret PID
    myPID.SetMode(MANUAL);
    Commande=0;
    Fait_PWMa(0); 
    
    // les resultats:
    //---------------En tete: 
    Serial.print(F("Periode d'echantillonnage Te= "));Serial.print(periodeEchantAvVit);Serial.println(F(" ms"));
    Serial.println(F("Correcteur: "));
    Serial.print(F("  Kp "));Serial.println(myPID.GetKp());
    Serial.print(F("  Ki "));Serial.println(myPID.GetKi());
    Serial.print(F("  Kd "));Serial.println(myPID.GetKd());               
    Serial.println(F("date;Consigne;Mesure; Commande"));
    Serial.println(F("[micros];[pt];[pt];[pt];[pt]"));
    Serial.print(0);Serial.print(F(";"));
    Serial.print(0);Serial.print(F(";"));
    Serial.print(0);Serial.print(F(";"));
    Serial.print(0);
    Serial.println();
    n=0;
    while (n<nb) {
         Serial.print(rest[n]);Serial.print(F(";"));
         Serial.print(Consigne,0);Serial.print(F(";"));
         Serial.print(resm[n]);Serial.print(F(";"));
         //Serial.print(Consigne-resm[n],0);Serial.print(F(";"));
         Serial.print(resc[n]);
         Serial.println();
        n++;
        }// fin while n< nb
    Serial.println();
  
    }  
//------------------------BOUCLE OUVERTE AVANCE--------------------------------------------
void Fait_BO_avance()
        {           
        long posinit;
        byte tension;
        tension=LireEntier(F("Entrer tension  (entier entre 0  et 9)"),0,9);

        //Serial.println(F("-- VA BOUGER !  !---"));
        //attente:
        for (int y=0; y<10;y++){ 
        for (int x=0 ; x< 30000; x++){if (x % 15000==0){      Serial.print(F("*"));} }};
        //Serial.println();  
            
        // recuperer la position initiale de l'encodeur:
        posinit=recupPosition();     
        date0=millis();
        Serial.println(posinit);
        analogWrite(PIN_COMMANDEa, 0);
        digitalWrite(PIN_DIRa,HIGH);
        Serial.println(F("date;Position;Courant"));
        Serial.println(F("[ms];[pt];[mA]"));
        analogWrite(PIN_COMMANDEa, int(255*tension/9.0)); 
        date=0;
        long posit;
        int courant;
        while (date<duree)
              {
                //**************************************************************************  
              
                  posit=recupPosition()-posinit;
                  date=millis()-date0;
                  // I=(1000*2*5*AnalogRead(A1) )/(3,3*1023) en mA
                  courant=analogRead(A1)*10/(3.3*1.023);
                  // imprimer date et position 
                  Serial.print(date);
                  Serial.print(F(";") );
                  Serial.print(posit);
                  Serial.print(F(";") );
                  Serial.println(courant);
                delay(10);
               } 
         analogWrite(PIN_COMMANDEa, 0);
        }              
// -------------------------------------------------------------------
void Fait_PWM(int y)  // commande moteur
    { if (y <0) { analogWrite(PIN_COMMANDE, 0);attend();digitalWrite(PIN_DIR,LOW);}
      else{analogWrite(PIN_COMMANDE, 0);attend();digitalWrite(PIN_DIR,HIGH);}
    attend();
    analogWrite(PIN_COMMANDE, abs(y));
     }

     // -------------------------------------------------------------------
void Fait_PWMa(int y)  // commande moteur
    { if (y <0) { analogWrite(PIN_COMMANDEa, 0);attend();digitalWrite(PIN_DIRa,LOW);}
      else{analogWrite(PIN_COMMANDEa, 0);attend();digitalWrite(PIN_DIRa,HIGH);}
    attend();
    analogWrite(PIN_COMMANDEa, abs(y));
     }
void attend(){for (int x=0 ; x< 5000; x++){if (x % 500==0){};}} 

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
    return   recompose(b[3],b[2],b[1],b[0]);
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
//-----------------------------------------------------------
float LireFlottant( String msg,float mi,float ma)
  {
      bool OK=false;
      float y;
      Serial.println(msg);
      while(OK== false){  
          while(Serial.available() > 0){       
              // recherche du prochain entier sur le port série:
              float iy = Serial.parseFloat();
              // encore:  
              // recherche du caractère nouvelle ligne pour terminer        
              if (Serial.read() == '\n'){ 
                               y = constrain(iy, mi,ma); 
                  OK=true;
              } 
          }
      }  
      return y;
    
  }
//----------------------------------------------------------------------------------  
float LireEntier( String msg,int mi,int ma)
  {
      bool OK=false;
      int y;
      Serial.println(msg);
      while(OK== false){  
          while(Serial.available() > 0){       
              // recherche du prochain entier sur le port série:
              int iy = Serial.parseFloat();
              // encore:  
              // recherche du caractère nouvelle ligne pour terminer        
              if (Serial.read() == '\n'){ 
                               y = constrain(iy, mi,ma); 
                  OK=true;
              } 
          }
      }  
      return y;
    
  }
//-----------------------------------------------------------------------------------
//-----------------------------------------------------------
// récupérer position virtuelle
 long recupPosition_v(long t)
 {
float tau=50000.0;   
return ( t-tau+long(tau*pow(2.718281828,-float(t)/tau)))/40.0;}
