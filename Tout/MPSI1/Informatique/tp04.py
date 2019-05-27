# -*- coding:iso-8859-1 -*-

# IPT
# AUTOMATIQUE DES S.L.C.I.: CONSTRUCTION DE L'ABAQUE DU T5%

import matplotlib.pyplot as plt
import numpy as np

epsi = 0.0001

# Exercice 1
#-------------------------------------------------------------------------------------
def dichotomie(f, a, b, epsi): # retourne une valeur approch�e du z�ro d'une fonction
# d�but lignes � construire !!!!!!!!!
    u=a
    v=b
    while v-u < epsi:
        w = (u+v)/2
        if f(u)*f(v) <= 0 : 
            v = w
        else : 
            u = w

u = 2

# fin lignes � construire !!!!!!!!!
    return u # valeur approch�e du z�ro de f
#-------------------------------------------------------------------------------------


#--------------------------------------------------------------------
def t5_critique(): # retourne le t5% en r�gime critique t5%
    ta = 0
    tb = 1
    while rep_critique(tb) < 95/100:
        tb = tb * 2
    f = lambda x: rep_critique(x) - 95/100
    return dichotomie(f, tb / 2, tb, epsi)
# -------------------------------------------------------------------



# Exercice 2 �l�ve
def t5_aperiodique(tab_m): # obtenir la liste des t5% des r�ponses pseudop�riodiques
    res = []
# d�but lignes � construire !!!!!!!!!



# fin lignes � construire !!!!!!!!!
    return res # retourne la liste des t5% correspondant � la liste des m donn�s
#--------------------------------------------------------------------
# exercice 3 �l�ve
def intervalle_t5(m): # obtenir l'intervalle dans lequel se trouve le t5%
                      # et l'ordonn�e 0.95 ou 1.05
# d�but lignes � construire !!!!!!!!!
    ta = 0
    tb = 999999999
    lim = 99999999

# fin lignes � construire !!!!!!!!!
    return ta, tb, lim # doit retourner ta, tb et lim

#--------------------------------------------------------------------
# exercice 4 �l�ve
def t5_pseudoperiodique(tab_m): # obtenir la liste des t5% des r�ponses pseudop�riodiques
    res = []
# d�but lignes � construire !!!!!!!!!



# fin lignes � construire !!!!!!!!!
    return res


# fonctions diverses A NE PAS MODIFIER!
# ------------------------------------------------------------------
def rep_critique(t): # cas m = 1 ; r�ponse temporelle � un �chelon unitaire
    return 1 - np.exp( - t) * (1 + t)

def rep_aperiod(t, m): # cas m > 1 ; r�ponse temporelle � un �chelon unitaire
    sqm21 = np.sqrt(m ** 2 - 1)
    t1 = 1 / (m - sqm21)
    t2 = 1 / (m + sqm21)
    return 1 - t1 / (t1 - t2) * np.exp(-t/t1) + 1 / (t1 - t2) * np.exp(-t/t2)

def rep_pseudo(t, m): # cas m < 1 ; r�ponse temporelle � un �chelon unitaire
    sq1m2 = np.sqrt(1 - m ** 2)
    phi = -np.arctan(sq1m2 / m)
    return 1 - np.exp(-m * t ) * np.sin(sq1m2 * t - phi ) / sq1m2

def Dk(k, m): # les depassements relatifs
    return np.exp(-k * np.pi * m / np.sqrt(1 - m * * 2))
#--------------------------------------------------------------------


#--------------------------------------------------------------------
#construction des listes

#Pour tester les exercices pr�c�dents

# ------------------------------------------------------------------
def test_exo1():
    # trac� r�ponse temporelle avec t5% cas r�gime critique
    les_t = np.array([i / 20 for i in range(300)])
    les_y = rep_critique(les_t)
    t5pourcent = t5_critique()
    plt.plot(les_t, les_y, 'g--')
    plt.plot(t5pourcent, rep_critique(t5pourcent), 'ro')
    plt.plot([0, 15], [0.95, 0.95])
    plt.grid(True, which = "both", ls = "-")
    plt.title('R�ponse temporelle r�gime critique')
    plt.show()

def test_abaque():
    # Ne fonctionne que si tous les exercices fonctionnent
    # ------------ m < 1
    Npts = 100
    les_mm1 = [ 0.1 * np.power( 10, i / Npts ) for i in range(Npts) ]
    les_t5pcm1 = t5_pseudoperiodique(les_mm1)
    # ------------ m > 1
    Npts = 50
    les_mp1 = [ 1 * np.power( 10, i / Npts / 1.4 ) for i in range(1, Npts) ]
    les_t5pcp1 = t5_aperiodique( les_mp1 )
    # ------------ m = 1
    t5pc1 = t5_critique()

    # les trac�s quand la partie pr�c�dente est bonne
    plt.plot( les_mm1, les_t5pcm1, 'r+', 1, t5pc1, 'b.', les_mp1, les_t5pcp1, 'g-' )
    plt.grid(True, which = "both", ls = "-")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
