from matplotlib import pyplot as plt
import numpy as np
from math import e

def trace(f, a, b, nb=200, afficher=True):
    x = np.linspace(a, b, nb)
    y = [f(i) for i in x]
    plt.plot(x, y)
    plt.show()

def expo(a): return e**a

def f(x): return x**2 - 2
#ou f = lambda x: x**2

def dicho(f, a, b, epsi, afficher_ab=False):
    while b-a > epsi:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
        if afficher_ab:
            print(a, b)
            plt.plot( (a, b), (f(a), f(b)) , 'o')
    #fin du while
    #print(a)
    return a

a, b = 1, 2
dicho(f, a, b, 0.001, True)
trace(f, a, b)
#trace(expo, -5, 2, 200, True)
trace(lambda x:e**x-x-x**2, -5, 3)



