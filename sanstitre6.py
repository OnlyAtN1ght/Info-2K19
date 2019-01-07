# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:10:06 2019

@author: provot
"""
from sanstitre5 import normalissssss

T=[0,4,5,6,0,2,0,1,0,2,3,0 ]
kkk=[0,0,2]

def produitparunmonome(T,monome):
    b = []
    
    for i in range(len(monome)-1):
        b.append(0)
    
    b += T
    

    for j in range(len(b)-1):
        b[j] *= monome[-1]
    
    return normalissssss(b)[1]

def produit(T,V):
    j = 0
    for i in V:
        j+=1
        U = []
        for k in range(j):
            U.append[0]
            
    


