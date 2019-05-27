#Exercice 1:

def somme(L):
	s=0
	for x in L:
		s+=x    #s prend la valeur s+x
	return s

def representant_normalisé(f):
    l=len(f)
    S=somme(f)
    RN=[]
    k=0
    while S!=0:
        S=S-f[k]
        RN.append(f[k])
        k+=1
    return RN
