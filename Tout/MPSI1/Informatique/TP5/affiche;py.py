def affiche(E):  # afficher la table 
    bord=37*'*'
    #chaine ='*____*_' pour mieux voir
    d='* '+6*'    * ' # etoile espace et 6 fois (4espace etoile espace)(6 caracteres)
    d='*_'+6*'____*_'
    print(bord)
    for i in range(11,5,-1): # de 11 à 5 exclu
        st=str(E[i])
        if len(st)==1 : st=' '+st
        d=d[:2+6*(11-i)]+st+d[4+6*(11-i):] # E[i] deux chiffres
    print(d)
    print(bord)
    d='*_'+6*'____*_'
    for i in range(6):
        st=str(E[i])
        if len(st)==2 : d=d[:2+6*i]+st+d[4+6*i:]
        else : d=d[:3+6*i]+st+d[4+6*i:]
    print(d)
    print(bord)
