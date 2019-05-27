#Exercice 4:
M=[[5,-6,7,-2], [11,2,-13,1], [4,101,3,8]]
'''def car1(M):
    for k in range(len(M)):
        print('(',end=' ')
        for i in range(len(M[k])):
            print(M[k][i],end=' ')
        print (')')'''

def ex4q1(n,c):
    s=str(n)
    L=len(s)
    return(' '*(c-L+1)+s+' ')

'''def indiceligne(M):
    m=1
    for k in range(len(M)):
        for i in range(len(M[k])):
            s=len(str(M[k][i]))
            if s>m:
                m=s
        print(m)'''

def indicecol(M):
    r=len(M[0])
    C=[0]*r
    for k in range(r):
        m=0
        for i in range(len(M)):
            s=len(str(M[i][k]))
            if s>m:
                m=s
        C[k]=m
    return C

def chaine(M):
    r=len(M[0])
    C=indicecol(M)
    for l in range(len(M)):
        print('(',end=' ')
        for c in range(r):
            print(ex4q1(M[l][c],C[c]),end='',)
        print(')')

#def  enaihc(M):
    #M=M.split(')(')

#EXERCICE 5:
def transpo(M):
    N=[[[]for k in range(len(M))]for i in range(len(M[0]))]
    for l in range(len(M)):
        for c in range(len(M[l])):
            N[c][l]=M[l][c]
    return N

#EXERCICE 6:
L=[[0,45,-12,23],[1,-8,-15,123],[4,12,32,0]]
def ex6(M,L):
    N=[[[]for k in range(len(M[0]))]for i in range(len(M))]
    for l in range(len(M)):
        for c in range(len(M[0])):
            N[l][c]=M[l][c]+L[l][c]
    return N
            
#Exercice 7:
def prod(M,L):
    N=[[[]for k in range(len(L[0]))]for i in range(len(M))]
    for l in range(len(N)):
        for c in range(len(N[0])):
            t=0
            for s in range(len(M[0])):
                t+=M[l][s]*L[s][c]
            N[l][c]=t
    return N

#Exercice 9:
import copy
'''old=[2,3,5,7]
#new=copy.copy(old)
#old=[2,3,5,[7,11]]
#new=copy.copy(old)
#new=copy.deepcopy(old)'''

#Exercice 10:
'''def reseq(T,B):
    Tinv=copy.deepcopy(T)
    t=0
    for i in range(len(T)):
        for k in range(len(T)):
            if i=k:
                t+=T[i][k]
            elif (i+k)%==1:
                Tinv[i][k]=-Tinv[i][k]'''
T=[[6,4,4],[0,2/3,-13/3],[0,0,1/2]]
B=[[16],[-10/3],[2]]
def reseq(T,B):
    Bcop=copy.deepcopy(B)
    sol=[0]*len(B) #liste solution de même longueur que B
    for i in range(1,len(T)+1): #on commence par le fin
        sol[-i]=Bcop[-i][0]/T[-i][-i] #on divise B[-i] par l'élément diagonal de T[-i]
        if i!=len(T):
            for k in range(1,i+1): 
                Bcop[-1-i][0]-=sol[-k]*T[-1-i][-k]# retranche au terme "suivant" de B le produit
                #des éléments non diagonaux de T avec les solutions déjà trouvées
    return sol

#Exercice 11:
def type1(T,h,k,a):
    Tcop=copy.deepcopy(T)
    for i in range(len(T)):
        Tcop[h][i]+=a*Tcop[k][i]
    return Tcop

def type2
    
            
            
                

    
    
        
    
    
        


    
            
        
    
    
