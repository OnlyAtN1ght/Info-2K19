# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:31:18 2019

@author: provot
"""

class Tableau:
    
    def __init__(self,tableau):
        self.tableau = tableau
        
        self.isNormalize = False
        
        self.check()
    
    def check(self):
        if len(0):
            self.isNormalize = True
        if list(l) == [0] * len(l):
            self.tableau = []
            self.isNormalize = True
        
        
    def normalize(self):
        if self.isNormalize:
            return self.tableau
            
        #Removing the fucking useless zeros at the end of the list
        j = len( self.tableau)-1
        while  self.tableau[j] == 0:
            j -= 1
            
            if j == -1:
                break
            
            self.tableau.pop()
            
        if j==-1:
            return ([])
        
        
        
""""  
        
 #Check if the list is empty
    if len(T) == 0:
        return ("",T)
    
        
    
    
    s = ""
    for i in range(len(T)):
        s += "{}x^{} + ".format(T[i],i)
    s = s[:-2])
    return (s,T)"""
    


if __name__=="__main__":
    t = [2,5,5,1,65,0,0,0]
    nigga = Tableau(t)
    nigga.normalize()
    print(nigga.tableau)