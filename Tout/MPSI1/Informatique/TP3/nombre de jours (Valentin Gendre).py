def R(a,b):
        r = a
        while r>=n:
                r-=b
        return r
    
def bixestile(a):
        if R(a,4)==0 and R(a,100)!=0:
                return 1
        if R(a,400)==0:
                return 1
        return 0
    
def mois(a):
        if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
                return 31
        if a==2:
                return 28
        return 30
    
def nbjour(jj,mm,aa,j2,m2,a2):
        p=0
        f=aa
        while aa!=a2:
                b=0
                if aa>=1582:
                        b=bixestile(aa)
                p=p+b+365
                aa+=1
        while mm!=m2:
                b=0
                if mm>m2:
                        b=mois(m2)
                        if m2==2 and f==a2 and bixestile(f)==1:
                            b+=1
                        p=p-b
                        m2-=1
                if mm<m2:
                        b=mois(mm)
                        if mm==2 and f==a2 and bixestile(f)==1:
                                b+=1
                        p=p+b
                        mm+=1
        p=p+(j2-jj)
        return p
