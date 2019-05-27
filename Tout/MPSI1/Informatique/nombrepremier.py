def leastprime(n):
    if n%2==0: return 2
    if n%3==0: return 3
    else:
        
        k=0
        while k**2<n:
            k=k+1
        i=5
        x=False
        while  x ==False:
            if i<=k:
                if n%i==0:
                    x = True
                else :
                    if (i+1)%6==0: i=i+2
                    else:
                        i=i+4
            else :
                i=n
                x=True
        return i

def decomp(n):
    k=0
    while k**2<n:
        k=k+1
    l=[]
    if n==1:
        return l
    while n!=1:
        if n%2==0:
            l.append(2)
            while n%2==0:
                n=n/2
        elif n%3==0:
            l.append(3)
            while n%3==0:
                n=n/3
        else:
            k=0
            while k**2<=n:
                k=k+1
            i=5
            x=False
            while  x ==False:
                if i<=k:
                    if n%i==0:
                        x = True
                    else :
                        if (i+1)%6==0: i=i+2
                        else:
                            i=i+4
                else :
                    i=n
                    x=True
            l.append(i)
            n=n/i
    return l
