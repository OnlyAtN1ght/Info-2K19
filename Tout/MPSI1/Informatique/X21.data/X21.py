# -*- coding: utf-8 -*-

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
import numpy as np	# importation de la librairie numpy renommée np
import matplotlib.pyplot as plt # importation de la bibliothèque matplotlib

# Lecture du fichier de mesures
rep = '~/Desktop/Informatique/TP/X21.data/' # à modifier; chemin absolu du répertoire des fichiers de mesures
nomFich = input('Écrire le nom de fichier (sans son extension): ')
nomComplet = rep + nomFich + '.csv'
ilExiste = os.path.isfile(nomComplet)
if not(ilExiste): exit()
f = open(nomComplet, 'r')
mes1 = f.readline().strip('\n\r') # QUESTION 1: que fait .strip('\n\r') ?
mes2 = f.readlines()
f.close()

# construction des listes
mes2 = mes2[3:]
t = []
pos = []
consigne = []
commande = []
for m in mes2:	# lecture des lignes pour construire les listes utiles
    m.strip('\n\r')
    tpc = m.split(';')		# QUESTION 2: que fait .split(';') ?
    t.append(int(tpc[0]))
    consigne.append(int(tpc[1]))
    pos.append(int(tpc[2]))
    commande.append(int(tpc[3]))

# Tracé des courbes et sauvegarde dans le dossier du script Python

# Valeur finale: elle est prise comme moyenne de 20 derniers points

# Calcul de l'erreur relative

# Détermination du temps de réponse à 5 pour cent
