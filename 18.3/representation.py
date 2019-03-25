from ex2 import g
from ex3 import h

import matplotlib.pyplot as plt
import numpy as np



def representation(fonction,borne_inf,borne_sup):
    X = [i for i in np.arange(borne_inf, borne_sup, 0.3)]
    Y = [fonction(j) for j in X]
    plt.plot(X,Y)
    plt.show()

def f(x):
    return x**3 -3*x +2

if __name__=="__main__":
    representation(f,-10,10)
