def diveuc(A,B):
    R=A[:]
    Q=[]
    while len(R)>=len(B):
        q=R[-1]/B[-1]
        Q=[q]+Q
        D=(len(R)-len(B))*[0]
        E=D+[q*X for X in B]
        R=[R[i]-E[i] for i in range(len(R))]
        R.pop()
    return Q, R
