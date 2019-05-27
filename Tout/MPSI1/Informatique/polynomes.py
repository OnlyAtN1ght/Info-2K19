# -*- coding:iso-8859-1 -*-

# cf.A08.py

## POLYNÔMES

# Les polynômes sont représentés par des tableaux
# a_0 + a_1 X + a_2 X ** 2 + ... -> [a_0, a_1, a_2, ...]

def clean(f):
    while len(f) > 0 and f[-1] == 0:
        f = f[:-1]
    if f == []:
        return [0]
    return f

def add(f, g):
    s = []
    f = clean(f)
    g = clean(g)
    F, G = len(f), len(g)
    for k in range(F):
        if k < G:
            s.append(f[k] + g[k])
        else:
            s.append(f[k])
    if F < G:
        for k in range(F, G):
            s.append(g[k])
    return clean(s)

def mult(f, g):
    m = []
    g = clean(g)
    try:
        f = clean(f)
        F = len(f)
        for k in range(F):
            z = []
            for h in range(k):
                z.append(0)
            z += mult(f[k], g)
            m = add(m, z)
    except TypeError: # f not a polynomial
        for y in g:
            m.append(f * y)
    finally:
        return clean(m)

# Produit d'un scalaire et d'un polynôme
def spmult(alpha, f, shift = 0):
    res = [0] * shift
    for x in f:
        res.append(alpha * x)
    return clean(res)

# Euclidean division
def EuclideanD(f, g):
    g = clean(g)
    if g == [0]: return 'Divisor null'
    # g normalisé
    if g[-1] != 1: return 'g monic!'
    n = len(g)
    r = f[:]
    q = []
    d = g[-1] * 1. # Python 2
    for k in range(len(f), n-1, -1):
        c = r[k-1] / d
        r[k-1] = 0
        q.append(c)
        for j in range(2, n+1):
            r[k-j] -= c * g[-j]
    return clean(q[::-1]), clean(r)

def Horner(f, x):
    y = 0
    for k in range(len(f)):
        y *= x
        y += f[-k-1]
    return y

def differentiate(f):
    f1 = []
    for k in range(1, len(f)):
        f1.append(k * f[k])
    return f1

def Newtonstep(f, x):
    # x = float(x)
    f1 = differentiate(f)
    y1 = Horner(f1, x)
    if y1 == 0: return 'Division par zéro'
    return x - Horner(f, x) / y1

def Newton(f, x):
    for n in range(50):
        x = Newtonstep(f, x)
    if abs(Horner(f, x)) > 1e-4:
        return 'Pas de zéro'
    return x

# quick exponentiation
def expn(f, n):
    if n == 0:
        return [1]
    if n == 1:
        return clean(f)
    u, v, m = 1, clean(f), n
    while m > 1:
        if m % 2 == 1:
            u = mult(u, v)
        m, v = m // 2, mult(v, v)
    return mult(u, v)

def polstr(f, reverse = True):
    s = ''
    F = len(f)
    for k in range(F):
        if reverse:
            s += str(f[-k-1]) + 'X^' + str(F-k-1) + '+'
        else:
            s += str(f[k]) + 'X^' + str(k) + '+'
    return s[:-1]

# Dernier exercice de P05.tex
# f = [1, -15, 77, -55, -1043, 4758, -9065, 7825, -3773, 5850, -3339, -6534, 1755, 2376, 432][::-1]
f = [432, 2376, 1755, -6534, -3339, 5850, -3773, 7825, -9065, 4758, -1043, -55, 77, -15, 1]
racines = [[-0.37442376320906406, 3], [4.0, 1], [-4.1163643904864671, 1], [0.86390855597514, 1]]

def weight(f):
    s = 0
    for x in f:
        s += abs(x)
    return s

def gcd(f, g):
    f = clean(f)
    g = clean(g)
    while weight(f) > 1e-6 and weight(g) > 1e-6:
        a = float(f[-1])
        b = float(g[-1])
        f = [ float(x) / a for x in f ]
        g = [ float(x) / b for x in g ]
        f, g = g, EuclideanD(f, g)[1]
    if weight(g) > 1e-6:
        return g
    return f

# def fraccont(x):
#    return
