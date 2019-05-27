# Exercice P06.2
# 1.
def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while a * b != 0:
        a, b = b, a % b
    return a + b

# 2.
def simpl(r):
    a = r[0]
    b = r[1]
    d = gcd(a, b)
    if b > 0:
        e = 1
    else:
        e = -1
    return [ e * a // d, e * b // d ]

# 3.
def op(r):
    return simpl([ -r[0], r[1] ])

def sm(r, s):
    return simpl([ r[0] * s[1] + r[1] * s[0], r[1] * s[1] ])

def pr(r, s):
    return simpl([ r[0] * s[0], r[1] * s[1] ])

#4.
# Pour n et k connue
def binom1(n, k):
    b = 1
    if k > n-k:
        k = n-k
    while k != 0:
        b = (n/k)*b
        k = k-1
        n = n-1
    return b

# Pour n et k inconnue
def binom10(n, k):
    b = [ 1, 1 ]
    if k > n:
        return 0
    if 2 * k > n:
        k = n - k
    for h in range(0, k):
        b = pr(b, [n-h, k-h])
    return b[0]

def binom2(n, k):
    if k > n:
        return 0
    if 2 * k > n:
        k = n - k
    b = [ 1, 1 ]
    for h in range(0, k):
        b = pr( b , [ n - h , h + 1] )
    return b[0]

def somme3(n):
    s = 0
    for k in range(1, n+1):
        s += (-1)**(k-1) * binom10(n, k) * k
    return s
