# -*- coding: utf-8 -*-

 #TODO ; chemin absolu du répertoire des fichiers de mesures

"""
Analyse de la réponse d'un système asservi en position

Rappel contenu fichiers de mesure:
L'en-tête contient des réglages susceptibles d'améliorer le comportement

colonne 0: le temps en millisecondes
colonne 1: la consigne en points (2000 points fait un tour du moteur)
colonne 2: la réponse du système en points
colonne 3: la commande envoyée au système (255 points donne 12 volts)
"""


import os
import numpy as np	
import matplotlib.pyplot as plt


# Lecture du fichier de mesures
#nomFich = input('Écrire le nom de fichier (sans son extension): ')

def main():
    path = "essai4.csv"
    
    if not os.path.isfile(path):
        exit()

        
    with open(path, 'r') as f:
        """
        QUESTION 1: que fait .strip('\n\r') ?
        Suprimme le retour a la ligne et le passsage a la ligne suivante a la fin de la premiere line
        """

        #Entete du fichier, inutile pour nous
        entete = f.readline().strip('\n\r')

        #Tableau avec toutes les donnees du csv et lesdonnees recuperees commencent a la troisieme ligne
        donnees = f.readlines()[3:]

    # construction des listes
    date = []
    pos = []
    consigne = []
    commande = []

    # lecture des lignes pour construire les listes utiles
    for donnee in donnees:
        """
        QUESTION 2: que fait .split(';') ?
        Separe la string en tableau en fonction de la string passee en argument
        """

        #Separe le csv par la string ';' car le csv n'est pas un csv mais un ; separate value
        tabl_donnee = donnee.split(';')

        #Ajoute toutes les donnes dans le bon tableau
        date.append(int(tabl_donnee[0]))
        consigne.append(int(tabl_donnee[1]))
        pos.append(int(tabl_donnee[2]))
        commande.append(int(tabl_donnee[3]))

    return date,pos
        
def plot(x,y):
    #Tracer les courbes 
    plt.plot(x,y) 
##    plt.ylabel('pos')
##    plt.xlabel("temps")
    plt.show()

def moyenne(mesure):
    total = 0
    for ele in mesure[-20:]:
        total += ele
    return total/20


if __name__ == "__main__":
    X , Y = main()

    print(moyenne(Y))


"""
Sauvegarde dans le dossier du script Python

Valeur finale: elle est prise comme moyenne de 20 derniers points

Calcul de l'erreur relative

Détermination du temps de réponse à 5 pour cent
"""
