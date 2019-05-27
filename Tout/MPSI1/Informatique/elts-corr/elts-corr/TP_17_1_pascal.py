# Quelques éléments sur TP1
#---------------------------------------
# 2.
# Fonction auxiliaire:
# Paramètres: des tableaux L et M.
# Résultat:
# attention!! cette fonction modifie le paramètre M;
# M devient lui-même complété des sommes successives de deux éléments 
# consécutifs de L.
def aux(L, M):
    for j in range(len(L) - 1):
        M.append(L[j] + L[j+1])
    return M

def pascal(n, k):
    # les instructions print(..) ne sont là que pour aider à comprendre,
    # ce qui compte c'est l'instruction return L[0]
    # les commentaires
    if k > n:
        return 0
    if 2 * k > n:
        k = n - k
    L = [1]                     #étape 0: fabrique ligne 0
    print(0,L)
    print('**************')
    for h in range(0, k):       #étape 1: fabrique ligne 1+0  à  1+k exclu
        L = aux(L, [1])
        L.append(1)
        print(h+1,L)            #juste pour voir le numéro de ligne h+1 et son contenu
    print('**************')
    for h in range(k, n-k):     #étape 3: fabrique lignes 1+k à  1+(n-k) exclu
        L = aux(L, [1])
        print(h+1,L)
    print('**************')
    for h in range(n-k, n):     #étape 4: fabrique lignes 1+ (n-k) à  1+n  exclu
        L = aux(L, [])
        print(h+1,L)    
    return L[0]


#3.3 Vérification de quelques formules

#Exercice 6
def C1(n):
    Res=0
    for i in range(n+1):
        Res=Res+binom1(n,i)*(-1)**i
    return Res
def testC1(N):
    test=True
    i=1
    while i<N+1 :
        test=(C1(i)==0)
        print(i,C1(i),' res= ',test)
        i+=1
    print('n= ',i-1,test)
