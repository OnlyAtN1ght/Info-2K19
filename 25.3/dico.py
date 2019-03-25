def dicotomie(f,a,b,e=10e-10):
    """
    Exercice 1.1
    Volé de 18.3/ex1.py
    """
    while b-a > e:
        c = (a+b)/2
        if f(a)*f(c)<=0:
            b=c
        else:
            a=c
    return a
