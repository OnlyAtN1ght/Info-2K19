# Travaux pratiques n°11 : Résolution d'équations différentielles

# Méthodes de résolution approchée d'équations différentielles résolues

# Exercice 1

def euler(f,a,A,tau,n):
    assert tau!=0
    T,X=[a],[A]
    for i in range(n):
        A=A+tau*f(a,A)
        a+=tau
        T.append(a)
        X.append(A)
    return T,X

def heun(f,a,A,tau,n):
    assert tau !=0
    T,X=[a],[A]
    for i in range(n):
        A=A+(1/2)*tau*(f(a,A)+f(a+tau,A+tau*f(a,A)))
        a+=tau
        T.append(a)
        X.Append(A)
    return T,X

# Exercice 2

def intervalle(a,b,n):
    A=[]
    for i in range(0,n+1):
        m=(1-(i/n))*a+(i/1000)*b
        A.append(m)
    return A

A=inter(-3,4,1000)

def valeur(A,n):
    B=[]
    for i in range(1000):
        B.append(A[i]**2)
    return B

#numpy.array pour transformer une liste en un tableau

A=array(A)
B=array(B)
matplotlib.pyplot.show(A,B)

# Exercice 3

A=linspace(0,10,100)
B=odeint(lambda x,t : x,1,A)
plot(A,B)
show()

# Exercice 4

#1.

A=linspace(0,10,1000)
B=odeint(lambda x,t:2*x**(1/2),1,A)
plot(A,B)
show()

#2.

L'une est nulle, t:t**2 est également solution.

On peut obtenir la seconde solution avec un pas nul.

# Exercice 5

#1.

#2. Pour tracer plusieurs courbes, on les trace d'abord puis seulement après on fait show.
#t0 est fixé.
# On remarque que plus t0 s'approche de 0, plus les deux courbes solutions se rapprochent l'une de l'autre. La courbe du dessous tend d'ailleur à devenir
# linéaire tandis que le renflement de celle du dessus à s'accentuer.

#3.

# Exercice 6

#2.
