import matplotlib.pyplot as plt
import numpy as np
import math

def dichotomie(f,a,b,e,borne=False):
    while b-a>e:
        c=(a+b)/2
        if f(a)*f(b)<=0:
            b=c
        else:
            a=c
    if(borne):
        print(a,b)
    return a
   
f=lambda x:x**3-3*x+2

g=lambda x:np.exp(x)-1-x**2

h=lambda x:np.exp(x)-x-2*x
    
def Trace_f(f,a,b):
    X=np.linspace(a,b,200)
    Y=[]
    for x in X:
        Y.append(f(x))
    plt.plot(X,Y,linewidth=2,color='r')
    
    
        