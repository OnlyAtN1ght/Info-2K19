def algo1(f,fd,a,e=10e-10):
    """
    Exercice 5.1.2
    """
    a = x
    b = a - f(a)/fd(a)
    while abs(b-a)>e:
        a,b = b,b-f(b)/fd(b)
    return b

def algo2(f,x,t=10e-10,e=10e-10):
    """
    Exercice 5.1.2
    """
    a = x
    b = a - 2*t*f(a)/(f(a+t)-f(a-t))
    while abs(b-a)>e:
        a,b = b,b - 2*t*f(b)/(f(b+t)-f(b-t))
    return b
