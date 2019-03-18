from ex3 import h
from ex2 import g

import math

def derivee (f,a,t=10e-10):
    """
    Exercie 4.2
    """
    return (f(a+t) - f(a-t))/(2*t)

def derivee_h():
    """
    Exercice 4.3
    """
    for e in [-2,-1,0,1,2]:
        print(derivee(h,e))

def d():
    """
    Exerice 4.4
    """
    def f(x):
        return math.exp(x) - 2*x -1

    print(derivee(f,1))
    
if __name__=="__main__":
    d()
    
