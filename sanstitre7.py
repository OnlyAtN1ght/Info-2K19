# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:31:18 2019

@author: provot
"""

class Polynome:
    
    def __init__(self,tableau):
        self.tableau = tableau
        
        self.isNormalize = False
        self.isMonome = False

        #Normalizing
        self.check()
        if not self.isNormalize:
            self.normalize()

        #Check if monome
        self.monome()
    
    def check(self):
        #Check if the list is empty or full of zeros and then normalize it 

        if len(self.tableau) == 0:
            self.isNormalize = True
        if self.tableau == [0] * len(self.tableau):
            self.tableau = []
            self.isNormalize = True
        

    def monome(self):
        number_of_zero = 0
        for i in self.tableau:
            if i == 0:
                number_of_zero += 1
        #If true it's a monome
        if number_of_zero == len(self.tableau)-1:
            self.isMonome = True


    def __add__(self,other):
        #Check type
        if type(other) != type(self):
            print("ERROR")
            return 0

        result = []
        if len(self.tableau) < len(other.tableau):
            self.tableau += [0]*(len(other.tableau)-len(self.tableau))
        if len(self.tableau) > len(other.tableau):
            other.tableau += [0]*(len(self.tableau)-len(other.tableau))

        for i in range(len(self.tableau)):
            result.append(self.tableau[i] + other.tableau[i])
        return Polynome(result)
    
    def __mul__(self, other):
        #Multiply polynome
     
        #Check type
        if type(other) != type(self):
            print("ERROR")
            return 0
        
        result = []

        #Make the tableaux the same lenght
        if len(self.tableau) < len(other.tableau):
            self.tableau += [0]*(len(other.tableau)-len(self.tableau))
        if len(self.tableau) > len(other.tableau):
            other.tableau += [0]*(len(self.tableau)-len(other.tableau))

        #If other or self is monome #FAUX
        if other.isMonome or self.isMonome:
            for i in range(len(self.tableau)):
                pass

            self.normalize()
            other.normalize()
            return Polynome(result)

        #If none are monome
        #Make the other polynome many monome
        #Prob just
        monomes = []
        for i in range(len(other.tableau)):
            s = ([0] * i) + [other.tableau[i]]
            monomes.append(Polynome(s))
        pres = []
        for monome in monomes:
            k = self * monome
            pres.append(k)
        result = Polynome([])
        for element in pres:
            result += element
        return result


      
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
        


if __name__=="__main__":
    t = [2,5,5,1,65,0,0,0]
    m = [0,0,0,0,0,1,0,0,0]
    test = [1,1,1]
    tab = Polynome(m)
    tab2 = Polynome(test)
    print(tab2.tableau)
    f = tab2*tab2
    print(f.tableau)
