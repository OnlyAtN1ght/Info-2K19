from dico import dicotomie

def f(x):
    return x**3 -3*x +2

if __name__=="__main__":
    print(dicotomie(f,-3,2)) # car f(-3) <0 et f(2) >0
