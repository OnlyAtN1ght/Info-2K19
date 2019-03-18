def dicotomie(f,a,b,e=10e-10):
    """
    Exercice 1.1
    """
    while b-a > e:
        c = (a+b)/2
        if f(a)*f(c)<=0:
            b=c
        else:
            a=c
    return a


def dicotomie(f,a,b,e=10e-10,afficher=False):
    """
    Exercice 1.3
    """
    while b-a > e:
        if afficher:
            print("Les bornes sont {} et {}".format(a,b))
        c = (a+b)/2
        if f(a)*f(c)<=0:
            b=c
        else:
            a=c
    return a
