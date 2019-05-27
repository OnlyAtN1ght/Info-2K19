def resolution_matrice_triangulaire(T,B):
    l=len(T)
    sol=[0 for i in range(0,l)]
    for i in range(l-1,-1,-1):
        somme=B[i]
        for j in range(l-1,i,-1):
            somme-=(T[i][j])*sol[j]
        sol[i]=somme/(T[i][i])
    return sol
    
