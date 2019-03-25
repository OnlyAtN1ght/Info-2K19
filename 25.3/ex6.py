import math
from dico import dicotomie

def fun(x):
    return math.exp(x) - 1 - 2*x

def zero_de_fun():
    """
    fun(-1) > 0
    fun(0.5) < 0
    fun(3) > 0
    """
    print(dicotomie(fun,-1,0.5))
    print(dicotomie(fun,0.5,3))




if __name__=="__main__":
    zero_de_fun()
