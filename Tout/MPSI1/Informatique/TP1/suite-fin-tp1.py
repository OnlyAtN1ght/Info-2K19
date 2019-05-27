# Exercice P06.1
# 1.
def op(r):
    return [ -r[0], r[1] ]

# 2.
def sm(r, s):
    return [ r[0] * s[1] + r[1] * s[0], r[1] * s[1] ]

# 3.
def pr(r, s):
    return [ r[0] * s[0], r[1] * s[1] ]

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
