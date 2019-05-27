#EXERCICE 1



def max2(L): #définition d'une fonction, avec en paramètre une  ligne L
    n = len(L)   #soit n la longueur de la liste
    if n == 1:   #on évacue le cas particulier ou la longueur de la liste = 1   
        return L[0] #on retourne alors la seule valeur présente dans la liste
    max = L[0] + L[1] #on définit max comme la somme des deux premiers élements de la liste, somme de départ
    for i in range(n-2): #on balaie tous les élements de la liste
        m = L[1+i] + L[2+i] #on associe à m la somme de deux éléments consécutifs de L
        if m > max: #si m (somme des deux éléments consécutifs) est supérieur à la somme maximum préalablement relevée
            max = m #alors on associe à la valeur max la valeur m
        
    return max #on renvoie alors la valeur max

#EXERCIE 2

def maxn(L, n):
    l = len(L)
    if l <= n:
        return sum(L)
   
    max = sum(L[0:n])     
        
    for i in range(l-n+1):
       m = sum(L[i:i+n])
       
       if m > max:
           max = m
           
    return max
        
print(maxn([0,8,8,2,2], 3))

#EXERCICE 3

def representation(Etat):
    Etat = Etat[:12]
    bord = 37 * '*'
    ligne = ''
# debut des lignes a modifier
    for i in range(6):
        ligne = ligne + '* ' + 4 * ' '
# fin des lignes a modifier
    ligne = ligne + '*'
    print(bord)

    ligne = ''
    
    for j in range(6, len(Etat)):
        st = str(Etat[j])
        if len(st) == 1: st = ' ' + st
        ligne = ligne + '* ' + st + 2 * ' ' 
     
    ligne += '*'
     
    print(ligne)
    ligne = str()
        
    for i in range(6):
        st = str(Etat[i])
        if len(st) == 1: st = ' ' + st
        ligne = ligne + '* ' + st + 2 * ' '

        
    ligne = ligne + '*'
    print(bord)
    print(ligne)
    print(bord)
    
#EXERCICE 4

def joue(E,n):
    k = n+1 
    for i in range(n+1, n+E[n]+1): 
        if i%12 == 0:
            k = 0
            
        E[k] += 1
        k+=1
        
    E[n] = 0
    E = E[0:6] + E[11:5:-1]
    
    representation(E)
    
def partie

tableau = [4]*12
joue(tableau,10)
    
    
    
    
       