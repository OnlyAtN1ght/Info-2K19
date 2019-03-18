import math

def g(x):
    """
    Exercice 2.1
    x|-> e^x - x - x^2 
    """
    return math.exp(x) - x - x**2

from ex1 import dicotomie

def zero_g():
    """
    Exercice 2.2

    g(-2) = -1.86466471676  < 0
    g(0)  = 1               > 0 
    """
    a = dicotomie(g,-2,0)
    return g(a)


"""
Exercice 2.3
lim g(x) = + inf (en + inf)
lim g(x) = - inf (en - ingf)
"""



if __name__ == "__main__":
    pass
