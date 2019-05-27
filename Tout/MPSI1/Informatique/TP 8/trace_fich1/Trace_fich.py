Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> A = [ 1 , 2 , 3 , 4 , 5 ]
>>> A[1]
2
>>> A[0]
1
>>> A[-1]
5
>>> A[2:4]
[3, 4]
>>> [2,-1]
[2, -1]
>>> [2:-1]
SyntaxError: invalid syntax
>>> [2 : -1]
SyntaxError: invalid syntax
>>> A[2:-1]
[3, 4]
>>> A[2:]
[3, 4, 5]
>>> A[:]
[1, 2, 3, 4, 5]
>>> A
[1, 2, 3, 4, 5]
>>> B = A[:]
>>> A
[1, 2, 3, 4, 5]
>>> B
[1, 2, 3, 4, 5]
>>> C=A
>>> A
[1, 2, 3, 4, 5]
>>> A[-1]=-1
>>> C=A
>>> C
[1, 2, 3, 4, -1]
>>> B
[1, 2, 3, 4, 5]
>>> 
>>> A[-1]=2018
>>> A
[1, 2, 3, 4, 2018]
>>> C
[1, 2, 3, 4, 2018]
>>> for k in range (1,4):
	k*i=k
	
SyntaxError: can't assign to operator
>>> i==1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    i==1
NameError: name 'i' is not defined
>>> i=1
>>> 3*i=
SyntaxError: invalid syntax
>>> 3*i
3
>>> for k in range (1,4)
SyntaxError: invalid syntax
>>> for k in range (1,4):
	i*k=i
	
SyntaxError: can't assign to operator
>>> i
1
>>> i==
SyntaxError: invalid syntax
>>> A==C
True
>>> A==B
False
>>> i==demande
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    i==demande
NameError: name 'demande' is not defined
>>> i=='demande'
False
>>> A[::-1]
[2018, 4, 3, 2, 1]
>>> 'Thibaut'
'Thibaut'
>>> [::]
SyntaxError: invalid syntax
>>> [::'']
SyntaxError: invalid syntax
>>> [:'']
SyntaxError: invalid syntax
>>> [::'thibaut']
SyntaxError: invalid syntax
>>> for k in range(1,32)
SyntaxError: invalid syntax
>>> for k in range (1,32):
	k=k+1
	i=k*i
disp k
SyntaxError: invalid syntax
>>> for k in range (1,32):
	i = k*i

>>> for k in range (1,32):
	i = k*i
print i
SyntaxError: invalid syntax
>>> for k in range (1,32):
	i = k*i
print i
SyntaxError: invalid syntax
>>> for k in range (1,32):
	i = k*i
print (i)
SyntaxError: invalid syntax
>>> for k in range (1,32):
	i = k*i
print(i)
SyntaxError: invalid syntax
>>> for k in range (1, 32):
	i = k*i
print(i)
SyntaxError: invalid syntax
>>> for k in range(1, 32):
	i = k*i
print(i)
SyntaxError: invalid syntax
>>> for k in range(1, 32):
	i = k*i

>>> print(i)
67615075532642592962076366156210530912566907412833894400000000000000
>>> thibaut[::]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    thibaut[::]
NameError: name 'thibaut' is not defined
>>> 'thibaut'[::]
'thibaut'
>>> 'thibaut'[::-1]
'tuabiht'
>>> s='abc'
>>> tuple (s)
('a', 'b', 'c')
>>> liat (s)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    liat (s)
NameError: name 'liat' is not defined
>>> list(s)
['a', 'b', 'c']
>>> U = tuple (s)
>>> T = list(s)
>>> str (T)
"['a', 'b', 'c']"
>>> 'ouioui'.join(U)
'aouiouibouiouic'
>>> '::'.join(U)
'a::b::c'
>>> .join(S)
SyntaxError: invalid syntax
>>> ''.join(U)
'abc'
>>> ''join(U) == S
SyntaxError: invalid syntax
>>> ''.join(U) == S
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    ''.join(U) == S
NameError: name 'S' is not defined
>>> ''.join(U)==S
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    ''.join(U)==S
NameError: name 'S' is not defined
>>> 'ouioui'.join(U)
'aouiouibouiouic'
>>> S = ''
>>> for x in T:
	S +=x

	
>>> S
'abc'
>>> for x in T:
	x

	
'a'
'b'
'c'
>>> 
>>> ## latin : catena: chaine
>>> for k in range(1,10)
SyntaxError: invalid syntax
>>> for k in range(1,10):
	k=k*(k-1)

	
>>> print(k)
72
>>> for k in range(1,10):
	k=k*(k)

	
>>> print k
SyntaxError: invalid syntax
>>> print (k)
81
>>> for k in range(1,12):
	k=k*(k)

	
>>> print (k)
121
>>> s ='J\'aime les mathématiques'
>>> s
"J'aime les mathématiques"
>>> print (s)
J'aime les mathématiques
>>> "je dois apprendre à mes étudiants les mathématques ".split"s"
SyntaxError: invalid syntax
>>> for i in range(10):
	print s
	
SyntaxError: invalid syntax
>>> for i in range(10):
	print (s)

	
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
>>> 10*(a+ '\n')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    10*(a+ '\n')
NameError: name 'a' is not defined
>>> 10*(s + '\n')
"J'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\n"
>>> 10*(s + ('\n'))
"J'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\nJ'aime les mathématiques\n"
>>> print(10 * (s + '\n')[:-1])
J'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiquesJ'aime les mathématiques
>>> print((10 * (s + '\n'))[:-1])
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
J'aime les mathématiques
>>> print((10 * ('\n' + s + '\n'))[:-1])

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques

J'aime les mathématiques
>>> split(s)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    split(s)
NameError: name 'split' is not defined
>>> a.reverse
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.reverse
NameError: name 'a' is not defined
>>> A.reverse()
>>> 
>>> a
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> A
[2018, 4, 3, 2, 1]
>>> A.sort()
>>> A
[1, 2, 3, 4, 2018]
>>> s.sort()
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    s.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> s
"J'aime les mathématiques"
>>> t = (list(s)).sort()
>>> t
>>> t = list(s)
>>> t
['J', "'", 'a', 'i', 'm', 'e', ' ', 'l', 'e', 's', ' ', 'm', 'a', 't', 'h', 'é', 'm', 'a', 't', 'i', 'q', 'u', 'e', 's']
>>> ''.join(t)
"J'aime les mathématiques"
>>> t.sort
<built-in method sort of list object at 0x025C1968>
>>> t
['J', "'", 'a', 'i', 'm', 'e', ' ', 'l', 'e', 's', ' ', 'm', 'a', 't', 'h', 'é', 'm', 'a', 't', 'i', 'q', 'u', 'e', 's']
>>> a = [1 , 2 , 3 , 4 )
SyntaxError: invalid syntax
>>> a = [1 , 2 , 3 , 4 ]
>>> b = [8 , 5 , 3 , 1 ]
>>> c = [9 , 5 , 4 , 9 ]
>>> a,b,c
([1, 2, 3, 4], [8, 5, 3, 1], [9, 5, 4, 9])
>>> (1 2 3 4 )
SyntaxError: invalid syntax
>>> (1 2 3 4 )
SyntaxError: invalid syntax
>>> a=(1 2 3 4 )
SyntaxError: invalid syntax
>>> a=( 1  2  3  4 )
SyntaxError: invalid syntax
>>> A=([1, 2, 3, 4], [8, 5, 3, 1], [9, 5, 4, 9])
>>> A
([1, 2, 3, 4], [8, 5, 3, 1], [9, 5, 4, 9])
>>> def f(x): return
1
SyntaxError: invalid syntax
>>> def f(x): return
f(1)
SyntaxError: invalid syntax
>>> 
>>> a = [1 , 2 , 3 , 4 )
SyntaxError: invalid syntax
>>> 
>>> 


>>> 


>>> 

>>> 



>>> 

>>> 


>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> def carre(x):
	return x**2
def (x,y):
	
SyntaxError: invalid syntax
>>> def carre(x):
	return x**2
def somme(x,y):
	
SyntaxError: invalid syntax
>>> carre(9)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    carre(9)
NameError: name 'carre' is not defined
>>> n= 1457
>>> c = 9
>>> s = '_'+'________'+str(n)+'_'
>>> 
>>> s
'_________1457_'
>>> lens)
SyntaxError: invalid syntax
>>> len(s)
14
>>> len(s)==9
False
>>> len(s)-c
5
>>> s = '_'+'_____'+str(n)+'_'
>>> len (s)==C+2
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    len (s)==C+2
TypeError: can only concatenate list (not "int") to list
>>> len (s)== (c+2)
True
>>> n=-1547
>>> c=9
>>> case(n, c)
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    case(n, c)
NameError: name 'case' is not defined
>>> exp(0)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    exp(0)
NameError: name 'exp' is not defined
>>> e(0)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    e(0)
NameError: name 'e' is not defined
>>> a=2.71
>>> 2.71**2
7.3441
>>> 2.71**3
19.902511
>>> 2.71**8
2909.071040502419
>>> 2.71**12
156903.08781896206
>>> 2.71**12
156903.08781896206
>>> 2.72**12
163993.58065535742
>>> 
