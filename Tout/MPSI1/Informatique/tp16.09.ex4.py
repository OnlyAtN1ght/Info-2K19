## NE PAS MODIFIER CE FICHIER.

# Exercice X03.1
## (  5   -6    7  -2 )
## ( 11    2  -13   1 )
## (  4  101    3   8 )

# 1.
def matrixelt(n, c):
    s = str(n)
    return (" " * (c + 1 - len(s))) + s + " "

# 2.
def maxlen(M):
    L = []
    rows, cols = len(M), len(M[0])
    for k in range(cols):
        L.append(max([len(str(M[h][k])) for h in range(rows)]))
    return L

# 3.
def viewmatrix(M):
    rows, cols = len(M), len(M[0])
    S = []
    L = maxlen(M)
    for h in range(rows):
        s = "("
        for k in range(cols):
            s += matrixelt(M[h][k], L[k])
        s += ")"
        if h < rows-1:
            s += "\n"
        S.append(s)
    return "".join(S)

# 4.
def makeline(s):
    while s[0] in [' ', '(', '\n']:
        s = s[1:]
    while s[-1] in [' ', '\n']:
        s = s[:-1]
    s = s.split()
    L = []
    for x in s:
        L.append(int(x))
    return L

def makematrix(Mstr):
    M = []
    while Mstr[0] in [' ', '(', '\n']:
        Mstr = Mstr[1:]
    while Mstr[-1] in [' ', '\n']:
        Mstr = Mstr[:-1]
    Mrows = Mstr.split(')')
    for line in Mrows:
        if len(line) > 0:
            M.append(makeline(line))
    return M
