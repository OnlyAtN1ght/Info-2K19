from ex1 import dicotomie

def h(x):
    """
    Exercice 3.1
    """
    return x**3 - 3*x +2

def zero_h():
    """"
    Exercice 3.2

    h(-3) = -16  < 0
    h(2)  = 4    > 0
    """
    a = dicotomie(h,-3,2)
    return a


""""
Exercice 3.3

Oui elle permet de le determiner avec une borne inf superieur au premier zero
et inferieur au deuxieme
"""

if __name__ == "__main__":
    print(h(zero_h()))
