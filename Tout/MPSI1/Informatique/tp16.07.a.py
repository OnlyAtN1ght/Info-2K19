import math

import matplotlib.pyplot as ppl

# Version 1:
def dichotomie(f, a, b, epsilon):
    u, v = a, b
    while v - u > epsilon:
        w = (u+v) / 2
        if f(u) * f(w) <= 0:
            v = w
        else:
            u = w
    return u

print(dichotomie(lambda x: x**2-2, 0, 2, 1e-4))

print (dichotomie(lambda x: x**2-2, 2, 0, 1e-4))

# Version 2:
def dichotomie(f, a, b, epsilon):
    if a > b:
        u, v = a, b
    else:
        u, v = b, a
    while v - u > epsilon:
        w = (u+v) / 2
        if f(u) * f(w) <= 0:
            v = w
        else:
            u = w
    return u

# Version 3:
def dichotomie(f, a, b, epsilon):
    if a > b:
        a, b = b, a
    while b - a > epsilon:
        c = (a+b) / 2
        if f(a) * f(c)<=0:
            b = c
        else:
            a = c
    return a

# Version 4:
def dichotomie(f, a, b, epsilon):
    if a > b:
        a, b = b, a
    while b - a > 2 * epsilon:
        c = (a+b) / 2
        if f(a) * f(c)<=0:
            b = c
        else:
            a = c
    return (a+b) / 2

print(dichotomie(lambda x: x**2-4, 3, 0, 1e-4))

# Version 5:
def dichotomie(f, a, b, epsilon):
    if a > b:
        a, b = b, a
    while b - a > 4 * epsilon:
        c = (a+b) / 2
        if f(a) * f(c)<=0:
            b = c
        else:
            a = c
    return (a+b) / 2

print(dichotomie(lambda x: x**2-4, 3, 0, 1e-4))

# Version 6:
def dichotomie(f, a, b, epsilon):
    if f(a) * f(b) > 0: return 'Mauvais choix du couple (a, b).'
    if a > b:
        a, b = b, a
    while b - a > 4 * epsilon:
        c = (a+b) / 2
        if f(a) * f(c)<=0:
            b = c
        else:
            a = c
    return (a+b) / 2

print(dichotomie(lambda x: x**2-4, 3, 5, 1e-4))
#'Mauvais choix du couple (a, b).'

# Version 7:
def dichotomie(f, a, b, epsilon, tableau = False):
    if f(a) * f(b) > 0: return 'Mauvais choix du couple (a, b).'
    if a > b:
        a, b = b, a
    while b - a > 4 * epsilon:
        c = (a+b) / 2
        if f(a) * f(c)<=0:
            b = c
        else:
            a = c
        if tableau:
            print([a, b])
    return (a+b) / 2

print(dichotomie(lambda x: x**2 - 3, 1, 2, 1e-8, True))

import matplotlib.pyplot as ppl

def f(x):
    return math.exp(x) - 1 - 2 * x

def ABSC(a, b, N = 100):
    return [(1 - k/N) * a + (k/N) * b for k in range(N+1)]

absc =ABSC (-3, 3)
ord = [f(x) for x in absc ]

ppl.plot(absc, ord)
ppl.show()

def F(x):
    return math.exp(x) - x - x**2

F(dichotomie(f, .1, 5, 1e-5, True))

## dérivation

def derivation(f, a, t):
    return (f(a+t)-f(a-t))/2/t

