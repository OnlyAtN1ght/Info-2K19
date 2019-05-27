#Exo1
#1) Des listes
L=[['Alain', '17 rue des Alpes', '451.23.22', 'amicale', 'mathématicien', '3.14.15.92'],['Bernard','12 rue des Etoiles','1.01.01.00','amicale','astronaute','9.99.999'],['Claude', '17 rue des Alpes', '451.22.23', 'professionnelle', 'aviateur', '9.87.65.43'],['Ernest', '3 avenue des Alsaciens','67.68.67.68','','']]
#2)
def prenom(L):
    M=[]
    for x in range(len(L)):
        M.append(L[x][0])
    return M

def adresse(L):
    N=[]
    for x in range(len(L)):
        N.append(L[x][1])
    return N
#3)

def job(y):
    O=[]
    for i in range(len(L)):
        if L[i][4]==y:
            O.append(L[i][0])
    return O
        
#4) Bases de données, algèbre relationnel

#Exo2
#1)
Q= [ ("A", 1, [("Alain", "Galois"), ("Bernard", "Fourier")]),
		("A", 2, [("Claude", "Poisson"), ("David", "Galois")]),
		("B", 1, [("Ernest", "Poisson"), ("Fulbert", "Galois")]) ]
def etudiant(l,n):
    E=[]
    for x in range(len(Q)):
        if (l,n)==(Q[x][0],Q[x][1]):
            E.append(Q[x][2][0][0])
            E.append(Q[x][2][1][0])
    return E

#3) D'abord découper la liste de départ
X=Q[0][2]
Y=Q[1][2]
Z=Q[2][2]
def etudiant2(l,n):
    if (l,n)==((Q[0][0],Q[0][1])):
               prenom(X)
    if (l,n)==((Q[1][0],Q[1][1])):
               prenom(Y)
    if (l,n)==((Q[2][0],Q[2][1])):
               prenom(Z)
    else:
               return


