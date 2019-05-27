# -*- coding:iso-8859-1 -*-

# IPT
# AUTOMATIQUE DES S.L.C.I.: CONSTRUCTION DE L'ABAQUE DU T5%

import matplotlib.pyplot as plt
import numpy as np

# Fonctions diverses, � NE PAS MODIFIER!
# --------------------------------------------------------------------------------
# Rappel: omega_0 = 1
def rep_critique(t): # cas m = 1 ; r�ponse temporelle � un �chelon unitaire
    return 1 - np.exp(-t) * (1 + t)

def rep_aperiod(t, m): # cas m > 1 ; r�ponse temporelle � un �chelon unitaire
    sqm21 = np.sqrt(m ** 2 - 1)
    t1 = m + sqm21
    t2 = m - sqm21
    return 1 - t1 / (t1 - t2) * np.exp(-t/t1) + 1 / (t1 - t2) * np.exp(-t/t2)

def rep_pseudo(t, m): # cas m < 1 ; r�ponse temporelle � un �chelon unitaire
    sq1m2 = np.sqrt(1 - m ** 2)
    phi = -np.arctan(sq1m2 / m)
    return 1 - np.exp( -m * t ) * np.sin( sq1m2 * t - phi ) / sq1m2

def Dk(k, m): # les d�passements relatifs
    return np.exp(-k * np.pi * m / np.sqrt(1 - m ** 2))
# --------------------------------------------------------------------------------

epsi = 0.0001

## Exercice 1
# 1.1.
# --------------------------------------------------------------------------------
def dichotomie(f, a, b, epsi): # retourne une valeur approch�e du z�ro d'une fonction
    u = a
    v = b
    while v-u > epsi:
        w = (u+v)/2
    if f(u)*f(w) <= 0:
        v = w
    else:
        u = w
    
    return u # valeur approch�e du z�ro de f
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# 1.2.
def t5_critique(): # retourne le t5% en r�gime critique t5%
    ta = 0
    tb = 1
    while rep_critique(tb) < 0.95:
        tb = tb * 2
    f = lambda x: rep_critique(x) - 0.95
    return dichotomie(f, tb / 2, tb, epsi)
# --------------------------------------------------------------------------------

## Exercice 2 (�l�ve)
# 2.2.
def t5_aperiodique(tab_m): # obtenir la liste des t5% des r�ponses pseudop�riodiques
    res = []
# d�but lignes � construire !!!!!!!!!
    for m in tab_m:
        ta = 0
        tb = 1
        while rep_aperiod(tb, m) < 0.95:
            tb = tb*2
        res.append(dichotomie(lambda x: rep_aperiod(x, m) - 0.95, tb/2, tb, epsi))
# fin lignes � construire !!!!!!!!!
    return res # retourne la liste des t5% correspondante � la liste des m donn�s
# --------------------------------------------------------------------------------

## Exercice 3 (�l�ve)
# 3.2.
def intervalle_t5(m): # obtenir l'intervalle dans lequel se trouve le t5%
                      # et l'ordonn�e 0.95 ou 1.05
# d�but lignes � construire !!!!!!!!!
    ta = 0
    tb = 999999999
    lim = 99999999
    k = 0
    Ta=(2 * np.pi)/(1 * np.sqrt(1 - m ** 2))
    while Dk(k, m) > 0.05:
        k = k+1
    ta = (k-1)*(Ta/2)
    tb = k*(Ta/2)
    if (k-1)%2 == 0:
        lim = 0.95
    else :
        lim = 1.05
# fin lignes � construire !!!!!!!!!
    return ta, tb, lim # doit retourner ta, tb et lim

# --------------------------------------------------------------------------------

## Exercice 4 (�l�ve)
# 4.2.
def t5_pseudoperiodique(tab_m): # obtenir la liste des t5% des r�ponses pseudop�riodiques
    res = []
# d�but lignes � construire !!!!!!!!!
    for m in tab_m :
        ta, tb, lim = intervalle_t5(m)
        res.append(dichotomie(lambda x: rep_pseudo(x, m) - lim, ta, tb, epsi))
# fin lignes � construire !!!!!!!!!
    return res

# --------------------------------------------------------------------------------
# Construction des listes

# Pour tester les exercices pr�c�dents

# --------------------------------------------------------------------------------
# 1.3.
def test_exo1():
    # trac� r�ponse temporelle avec t5% cas r�gime critique
    les_t = np.array([i / 20 for i in range(300)])
    les_y = rep_critique(les_t)
    t5pourcent = t5_critique()
    plt.plot(les_t, les_y, 'g--')
    plt.plot(t5pourcent, rep_critique(t5pourcent), 'ro')
    plt.plot([0, 15], [0.95, 0.95])
    plt.grid(True, which = 'both', ls = '-')
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
    plt.grid(True, which = 'both', ls = '-')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
