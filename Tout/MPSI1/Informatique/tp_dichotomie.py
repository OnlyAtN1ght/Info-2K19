import matplotlib.pyplot as plt
import numpy as np

nbr_points=1000

def F(x):
    return x**3-3*x+2
def G(x):
    return np.exp(x)-x-x**2
def H(x):
    return np.exp(x)-1-2*x

a=-2.5
b=0.5
epsi = 0.01

intervalle=b-a
A=a
B=b

while (b-a)>epsi:
    c=(1/2)*(b+a)
    if F(a)*F(c) <=0:
        b=c
    else:
        a=c

z1 =(a+b)/2
print(z1)

X=[]
Y=[]


for i in range(0, nbr_points):
    X.append(A+((intervalle/nbr_points)*i))
    Y.append(F(X[-1]))

plt.plot(X,Y,'c-',[z1],[F(z1)],'bo')

b=B
a=A

while (b-a)>epsi:
    c=(1/2)*(b+a)
    if G(a)*G(c) <=0:
        b=c
    else:
        a=c

z2 =(a+b)/2
print(z2)

X=[]
Y=[]


for i in range(0, nbr_points):
    X.append(A+((intervalle/nbr_points)*i))
    Y.append(G(X[-1]))

plt.plot(X,Y,'y-',[z2],[G(z2)],'yo')

b=B
a=A

while (b-a)>epsi:
    c=(1/2)*(b+a)
    if H(a)*H(c) <=0:
        b=c
    else:
        a=c

z2 =(a+b)/2
print(z2)

X=[]
Y=[]

for i in range(0, nbr_points):
    X.append(A+((intervalle/nbr_points)*i))
    Y.append(H(X[-1]))

plt.plot(X,Y,'m-',[z2],[H(z2)],'mo')
plt.plot([A,B],[0,0],'k--')

plt.show

