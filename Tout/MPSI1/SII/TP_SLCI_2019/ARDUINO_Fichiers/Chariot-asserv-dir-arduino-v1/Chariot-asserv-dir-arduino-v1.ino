/**************************************************************
 * Asservissement de position direction du chariot filoguide  *
 * Juillet 2015                                               *
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
                                           v 2
Choix :
    - Etalonnage potentiometre          --->   1
    - Asservissement position direction --->   2



/*
  Lecture de Kp, Ki et Kd
separes par une virgule et contraints a rester dans un intervalle precis
L'echelon est choisi entre 0 et 60 .
*/

//-------------------------------------------------------------------------------
#include <PID_v1.h>
// pour le moteur et le potentiometre
//Potentiometre :Alimentation vert =5V,jaune=Gnd
//                Mesure bleu 
#define  PIN_MESURE 7   //mesure du potentiometre de direction
//Moteur :
#define PIN_DIR 12   // direction moteur direction A
#define PIN_COMMANDE 3 // power du moteur A  (c'est une PWM)
// shield moteur M+  = le blanc ; M- : le noir 

// ************************************************************************************

const int nb=150;  // nombre de points de mesure 150
const int periode_echant=8; // periode echantillonnage

// ************************************************************************************
//  apres etalonnage du potentiometre:
const float zero_mes=720;
const float inc_deg=3.0056;
//
double Consigne, Mesure, Commande;  // grandeurs en points
long unsigned date,date0;
//Valeur par defaut du PID
double ech,Kp=1.0, Ki=0, Kd=0;
PID myPID(&Mesure, &Commande, &Consigne, Kp, Ki, Kd, DIRECT);// ancienne position

void setup()
  {
  pinMode(PIN_DIR, OUTPUT); 
  pinMode(PIN_COMMANDE, OUTPUT);
  Serial.begin(115200); // initialisation port serie, choix debit

  }

void loop()
  {
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   int choix=choisirMenu();
   switch (choix) {
    case 0:  // rien    
       Serial.println(" ");       
       break;         
 
    case 1:  // etalonnage potentiometre
         Serial.println(F(" "));
         Serial.println(F("Etalonnage du potentiometre "));
        while ((Serial.read() != '\n')){
          int mesureAngle = analogRead(PIN_MESURE);    // lecture PIN_MES:
          Serial.print(F("mesure = "));Serial.print(mesureAngle);Serial.print(F(" pt  ")); 
          Serial.print(mesureAngle*5/1023.0,3);Serial.println(F(" V "));// imprime sur la sortie serie:
          delay(400);   // attente 400ms
          } 
        break;      
	  
    case 2:
       // cas direction BF echelon position: 
                Serial.println(F(" "));
                Serial.println(F(""));
                Serial.println(F("        Asservissement de position de la direction :"));
                Serial.println(F(""));
 // choix correcteur--------------------------------------------------------------------------                
                Serial.println(F("  Correction : entrer Kp, Ki et Kd flottants positifs separes par des virgules"));
                Serial.println(F(" Kp [0..20] Ki[0.. 5]  Kd[0.. 5]"));
               
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
                          iKp = constrain(iKp, 0, 20);    //limiter Kp
                          iKi =constrain(iKi, 0, 5);    // limiter Ki 
                          iKd =constrain(iKd, 0, 5);    // limiter Kd
                
                          // affiche :
                          Serial.print(F("  Kp= "));
                          Serial.print(iKp);
                          Serial.print(F("   "));
                          Serial.print(F("Ki= "));
                          Serial.print(iKi);
                          Serial.print(F("   "));
                          Serial.print(F("Kd= "));
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
                 
                 // choix echelon---------------------------------------------------------------------
                // lecture de la position initiale:
               int pos_init=analogRead(PIN_MESURE)-zero_mes;
                 float pos_init_deg=pos_init/inc_deg;
                 Serial.print(F("  Position initiale:  "));Serial.print(pos_init_deg,2);Serial.println(F("  degres "));    
                Serial.println(); 
                Serial.println(F("  Echelon:  Entrer un echelon compatible  avec une position finale dans [-60 ..60]"));
                OK=false;              
                while(OK== false){
                  // si quelque chose sur port serie,le lire :  
                  while (Serial.available() > 0) {               
                        // recherche du prochain entier sur le port serie:
                        float iech = Serial.parseFloat();         
                        // recherche du caractère nouvelle ligne pour terminer                  
                        if (Serial.read() == '\n') {
                          // constraint la valeur dans un intervalle
                          ech = constrain(iech,-60-pos_init_deg ,60-pos_init_deg );    //limiter Kp              
                          // affiche :
                          Serial.print(F("  Echelon= "));
                          Serial.print(ech);Serial.println(F("  degres"));
                          OK=true;
                        } // fin if Serial
                     Serial.println(F("--------------------")); 

                   };// fin while Serial.available
                 }// fin while OK false               
                 //fin choix echelon
                 
               //  PID myPID(&Mesure, &Commande, &Consigne, Kp, Ki, Kd, DIRECT);// ancienne position pas bon!!!!!
                
                 // petite attente:
                 for (int y=0; y<10;y++){ 
                   for (int x=0 ; x< 30000; x++){if (x % 15000==0){      Serial.print("*");} }
                   };
                 Serial.println("");  
                
                 //initialisation des variables

                 pos_init=analogRead(PIN_MESURE)-zero_mes;
                 Mesure=pos_init;
                 Consigne = int(ech*inc_deg)+pos_init; //         

                 myPID.SetOutputLimits(-255, 255);
                 myPID.SetSampleTime(periode_echant);  // Periode d'echantillonnage en ms   ******* 
                     
                
                 //++++++++++++++++++++++++++++++++++              
                 //activation PID       
                 myPID.SetMode(AUTOMATIC);
                 myPID.SetTunings( Kp,  Ki,  Kd);             
                 // ------------------------------  fin entree  
                 // lancement du mouvement 
                 date0=millis();                
                 int n= 0;
                 bool encore=true;
                 int resc[nb];  // avant  : double
                 int resm[nb]; //  avant : double
                 unsigned int rest[nb];
                 unsigned int resi[nb];
                 bool calcule;
                 Commande=0;
                 while (n<nb) {

                    Mesure = analogRead(PIN_MESURE)-zero_mes;
                    calcule=myPID.Compute();           
                    if (calcule) {        
                        resc[n]=int(Commande);  
                        resm[n]=int(Mesure);
                        rest[n]=millis()-date0;
                        resi[n]=analogRead(A0);//lecture courant        
                        //Serial.println(n);
                        Fait_PWM(int(Commande));
                        n++;
                        }
                  } // fin while n<nb
                  //myPID.SetMode(MANUAL);
                  Fait_PWM(0);
                 
                 Serial.print(F("Kp "));Serial.println(myPID.GetKp());
                  Serial.print(F("Ki "));Serial.println(myPID.GetKi());
                  Serial.print(F("Kd "));Serial.println(myPID.GetKd()); 
                  Serial.print(F("Mesure initiale [pt] : "));Serial.println(pos_init);// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                  Serial.print(F("Consigne [pt] : "));Serial.println(Consigne-pos_init);// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                 Serial.println(F("  date; Consigne; Sortie; Im_Cons; Mesure; Commande; Courant"));
                 Serial.println(F("  [ms]; [degre]; [degre]; [pt];  [pt];  [pt]; [mA]"));
                  n=0;
                  while (n<nb) {
                    Serial.print(rest[n]);Serial.print(F(" ;  "));
					 Serial.print((Consigne-pos_init)/inc_deg);Serial.print(F(" ;  "));
                     Serial.print((resm[n]-pos_init)/inc_deg);Serial.print(F(" ;  "));
					Serial.print(Consigne-pos_init,0);Serial.print(F(" ;  "));
                     Serial.print(resm[n]-pos_init);Serial.print(F(" ;  "));
                    Serial.print(resc[n]);Serial.print(F(" ;  "));Serial.println(resi[n]*10/(3.3*1.023),0);
                    n++;
                    }// fin while n< nb
                 Serial.println("");
                   
                 Serial.println("");
                 Serial.println(F(" Entree pour retour au menu"));
                 Serial.println("");           
 //                myPID.SetMode(MANUAL); 
                 Fait_PWM(0);
                 OK=false;
                 while((Serial.read() != '\n')){}  // boucle infinie
       break;
       //fin cas  dir echelon  cas 2
    } // fin switch	  
	   
   
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  Serial.println(F("  "));
  Serial.println(F(" Entree pour revenir au menu"));
  while((Serial.read() == '\n')){}  // boucle infinie  
  } //fin void loop

//------------------------------------------------------------------------
  int choisirMenu()
  {  
  Serial.println(F(""));
  Serial.println(F("      ********************************************"));
  //Serial.println(F("      *                                          *"));
  Serial.println(F("      *            CHARIOT FILOGUIDE             *"));
 // Serial.println("      *                                          *"));
  Serial.println(F("      ********************************************"));
  Serial.println(F("                                              v2"));
  Serial.println(F(""));
  Serial.println(F("   Choix :"));
  Serial.println(F("      - Etalonnage potentiometre                   --->   1"));
  Serial.println(F("      - Asservissement en position de la direction --->   2"));
  Serial.println(F("              (.... et Entree)"));
 
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
// -------------------------------------------------------------------

void Fait_PWM(int y)  // commande moteur
    { if (y <0) { analogWrite(PIN_COMMANDE, 0);attend();digitalWrite(PIN_DIR,LOW);}
      else{analogWrite(PIN_COMMANDE, 0);attend();digitalWrite(PIN_DIR,HIGH);}
    attend();
    analogWrite(PIN_COMMANDE, abs(y));
     }
     
void attend(){for (int x=0 ; x< 5000; x++){if (x % 500==0){};}} 
