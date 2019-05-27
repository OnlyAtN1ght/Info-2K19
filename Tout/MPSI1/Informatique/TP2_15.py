# Ex. 1
type(13)

type("MPSI1")

type("MPSI1"[2])

type(.1)

type(5**6)

type(2==2)

# Ex. 2

type(str(27))

# Ex. 3
x = "rouge"
y = "vert"
z = "jaune"
print(x,y,z)
z = x
print(x,y,z)
x = 0
print(x,y,z)

# Ex. 4
# 4.1
len(4)  # donne un erreur un entier n'a pas de longueur

len([4, 4., -.1, .1, "a"])
len(range(7))
len(range(5,9))
len("Que c'est long!")

# 4.2
(4, "pair", 5, "premier")[-2]
[4, 4., -.1, .1, "a"][-2]
range(7)[-2]
range(5,9)[-2]
"Que c'est long!"[-2]

# Ex. 5
3 and "a"
3 or "a"
"a" and 0
0 and "a"
0 or "a"
"a" or 0
0 or 0
"a" or 3
3 or "a"
True and 2
2 and True
True or 0
True or 2
2 or True

for x in range(3):
   for y in range(3):
       print( x, y)
       print( x and y)
       print (x or y)

# Ex. 6
L = []
n = 0
A = 2**20
while n**3 < A:
   L.append(n**3)
   n += 1
L

## ou mieux
L = []
n, c = 0, 0
A = 2**20
while c < A:
   L.append(c)
   c = n**3
   n += 1


# Ex. 7
for x in "Que c'est long!":
   print (x)

# Ex. 8
# 1.
def str2num(s): # choix de représentation le chiffre de poids fort
                #  1 si positif, 0 si négatif
                # il faut les zéros jusqu'au poids fort : 0000 != 000
   l = len(s)
   n = 0
   for k in range(l):
       n += int(s[k]) * 2**(l-k-1)
   return n - 2**(l-1)  # enlever 

# 2.
def num2str(n,l):
   n += 2**(l-1)  #on ajoute  2^(l-1)
   s = ""
   while n != 0:
       s += str(n%2)
       n //= 2
   s += "0"*(l-len(s))
   return s[::-1]  # 'retourne' s

# 3. Afficher les chaînes représentant nb -2^(l-1)<= n< 2^(l-1)
l = 5
n = -2**(l-1)
while n < 2**(l-1):
   print (num2str(n,l))
   n += 1

#4
#4.1
   #représenter l'opposé d'un nombre n donné par sa représentation
def oppose(s): # pas d'opposé à -2^(l-1)
   return num2str(-str2num(s),len(s))
# 4.2
def add(s,t):
   return num2str(str2num(s) + str2num(t), len(s))


#5 convention du complément à 2
#5.1
def str22num(s): # choix de représentation le chiffre de poids fort
                #  1 si positif, 1 si négatif
                # il faut les zéros jusqu'au poids fort : 0000 != 000
   l = len(s)
   n = 0
   for k in range(1,l):
       n += int(s[k]) * 2**(l-k-1)
   return n - int(s[0])*2**(l-1)  # enlever
#5.2
def num22str(n,l): # valable pour n negatif
   s0="0"	
   if (n<0) :
	   s0="1" 
	   n += 2**(l-1)  #on ajoute  2^(l-1) si negatif
   s = ""
   while n != 0:
       s += str(n%2)
       n //= 2
   s += "0"*(l-len(s)-1)
   s+=s0
   return s[::-1]  # 'retourne' s


