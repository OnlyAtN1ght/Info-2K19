# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:54:20 2019

@author: provot
"""
z=0

def normalissssss(T):
    """
    :param T : list to normalissssss
    :return : tuple of the string normalissssss and the list normalissssss
    
    """
    
    #Check if the list is empty
    if len(T) == 0:
        return ("",T)
    
        
    #Removing the fucking useless zeros at the end of the list
    j = len(T)-1
    while T[j] == 0:
        j -= 1
        if j == -1:
            break
        T.pop()
    if j==-1:
        return ("",[])
    
    s = ""
    for i in range(len(T)):
        s += "{}x^{} + ".format(T[i],i)
    s = s[:-2]
    return (s,T)
    
def mlong(T,V):
    a=normalissssss(T)[1]
    b=normalissssss(V)[1]
    if len(a) == len(b):
        return(a,b)
    if len(a) > len(b):
        for i in range(len(a)-len(b)):
            b.append(z)
    else:
        for i in range(len(b)-len(a)):
            a.append(z)

    return(a,b)

def somme(T,V):
    T,V=mlong(T,V)
    for i in range(len(T)):
        V[i]+=T[i]
    return V
   
#T=[0,4,5,6,0,2,0,1,0,2,3,0 ]
#V=[2,5,1,4,6,9,8]

#print(somme(T,V))