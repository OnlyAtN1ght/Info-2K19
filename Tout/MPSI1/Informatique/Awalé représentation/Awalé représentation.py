def representation(Etat):
    bord = 37 * '*'
    ligne = ''
    for i in range(6):
        b=11-i
        gr = str (Etat[b])
        if len(gr) == 1: gr = ' ' + gr
        ligne = ligne + '* ' + gr + 2 * ' '
    ligne = ligne + '*'
    print(bord)
    print(ligne)
    ligne = ''
    for i in range(6):
        st = str(Etat[i])
        if len(st) == 1: st = ' ' + st
        ligne = ligne + '* ' + st + 2 * ' '
    ligne = ligne + '*'
    print(bord)
    print(ligne)
    print(bord)
    
def joue(E, indice):
    k=(indice+1)%12
    while(E[indice]>0):
        E[indice]=E[indice]-1
        E[k]=E[k]+1
        k=k+1
        
