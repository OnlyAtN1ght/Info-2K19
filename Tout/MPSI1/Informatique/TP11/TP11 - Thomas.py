#Exercice 4 :
##Question 1 :
def chaine_1(n,c):
    s = str(n)
    l = len(s)
    return " " * (c+1-l) + s + " "

##Question 2 :
def chaine_2(M):
    ligne = len(M)
    colonne = len(M[0])
    L = []
    for z in range(colonne):
        X = []
        for k in range(ligne):
            X.append(len(str(M[k][z])))
        L.append(max(X))
    return L

##Question 3 :
def chaine_3(M):
    ligne = len(M)
    colonne = len(M[0])
    L = chaine_2(M)
    s = ""
    for k in range(ligne):
        t = "("
        for z in range(colonne):
            t += chaine_1(M[k][z],L[z])
        s += t + ')\n'
    print(s)

"M = [[5,-6,7,-2], [11,2,-13,1], [4,101,3,8]]"



#Exercice 9 :
##Question 1 :
"""
old=[2,3,5,7]
copy.copy(old)
new[3]=8
"""
"Les commandes 'new=copy.copy(old)' et 'new = old[:]' marchent avec cette méthode"

##Question 2 :
"""
old=[2,3,5,[7,11]]
new=copy.deepcopy(old)
new[3][0]=8
"""
"Les commandes 'new=copy.copy(old)' et 'new = old[:]' ne marchent pas avec une liste de listes car une modification d'un élément d'une liste entraîne la modification de l'élément de l'autre liste"



#Exercice 10 :
##Question 1 :
def matrice(T,B):
    n = len(T)
    X = [0 for i in range(n)]
    for k in range(n-1,-1,-1):
        S = 0
        for i in range(n):
            S += X[i]*T[k][i]
        X[k] = (B[k]-S)/T[k][k]
    return X

        
    










