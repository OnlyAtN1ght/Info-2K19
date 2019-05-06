from math import exp, sin, cos, log

def g(x):
    return x ** 3 - 3 * x + 2

def h(x):
    return exp(x) - x - x ** 2

def h1(x):
    return exp(x) - 1 - 2 * x

def dicho0(f, a, b, epsilon = 1e-15):
    while b - a > epsilon:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return a

def dicho1(f, a, b, epsilon = 1e-15):
    while b - a > epsilon:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def dicho2(f, a, b, epsilon = 1e-15):
    if a > b: a, b = b, a
    assert f(a) * f(b) <= 0
    while b - a > epsilon:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def dicho3(f, a, b, epsilon = 1e-15, aff = False):
    if a > b: a, b = b, a
    assert f(a) * f(b) <= 0
    while b - a > epsilon:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
        if aff: print([a, b])
    return (a + b) / 2

def NewtonD(f, f1, x, epsilon = 1e-15, aff = False):
    a = x
    b = a - f(a) / f1(a)
    while abs(b - a) > epsilon:
        a, b = b, b - f(b) / f1(b)
        if aff: print(b)
    return b

def NewtonS(f, x, t = 1e-5, epsilon = 1e-15, aff = False):
    a = x
    b = a - 2 * t * f(a) / (f(a+t) - f(a-t))
    while abs(b - a) > epsilon:
        a, b = b, b - 2 * t * f(b) / (f(b+t) - f(b-t))
        if aff: print(b)
    return b

def der(f, x, t = 1e-5):
    return (f(x+t) - f(x-t)) / 2 / t
