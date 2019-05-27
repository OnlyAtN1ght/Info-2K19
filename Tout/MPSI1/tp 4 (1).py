from math import *
n = 43
def diviseur_premier(n):
    l=[]
    j=0
    while j<sqrt(n):
        
        if n==1:
            print(n, " n'a pas de diviseur premier !")
        elif n%2==0:
            print("2 est le plus petit diviseur premier de ", n, " !!!!!")
            l.append(2)
        elif n%3==0:
            print("3 est le plus petit diviseur premier de ", n, " !!!!!")
            l.append(3)
        else:
            k = sqrt(n)
            i = 1
            t = 0
            while i<k:
                if 6*i-1 in l:
                    i = k
                elif n%(6*i-1)==0:
                    print(6*i-1, " est le plus petit diviseur premier de ", n)
                    t = 1 
                    i = k
                    l.append(6*i-1)
                elif 6*i+1 in l:
                    i = k
                elif n%(6*i+1)==0:
                    print(6*i+1, " est le plus petit diviseur premier de ", n)
                    i = k
                    t = 1
                    l.append(6*i+1)
                else:
                    i=i+1
            if t == 0:
                print(n, " est premier")
            j = j+1
            print(l)
diviseur_premier(n)


