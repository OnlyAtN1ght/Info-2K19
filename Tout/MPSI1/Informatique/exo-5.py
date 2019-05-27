# --------------------------------------------------------------------------------

## Exercice 5 (élève): le tracé doit montrer les discontinuités de l'abaque
def test_abaque_ameliore():
    # Ne fonctionne que si tous les exercices fonctionnent
    # Construction des listes de m et de t5 pourcent
    # ------------ m < 1
    Npts = 50
    les_mm1 = [ 0.1 * np.power( 10, i / Npts ) for i in range(Npts) ]
    les_t5pcm1 = t5_pseudoperiodique(les_mm1)
    # ------------ m > 1
    Npts = 50
    les_mp1 = [ 1 * np.power( 10, i / Npts / 1.4 ) for i in range(1, Npts) ]
    les_t5pcp1 = t5_aperiodique( les_mp1 )
    # ------------ m = 1
    t5pc1 = t5_critique()

    
    # initialisation des deux listes principales pour les m et les t5% correspondant 
    les_m=[]
    les_t5pc=[]

#+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# debut des modifications:
    les_m=[les_mm1]
    les_t5pc=[les_t5pcm1]

    
# fin de modifications
#+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +


    # on agrandit le dernier element de chaque liste principale
    # avec le point critique et la liste des m > 1 et celle des t5%
    les_m[-1] = les_m[-1]+[1]+les_mp1
    les_t5pc[-1] = les_t5pc[-1]+[t5pc1]+les_t5pcp1

    # tracé des lignes :
    for i in range(len(les_m)):
        plt.plot(les_m[i],les_t5pc[i],'r-',linewidth=2.0) # tracé d'une partie continue de la courbe
   
    plt.grid(True, which = 'both', ls = '-')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

# --------------------------------------------------------------------------------
