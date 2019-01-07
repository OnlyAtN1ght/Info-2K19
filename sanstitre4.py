# -*- coding: utf-8 -*-

def normalissssss(T):
    """
    :param T : list to normalissssss
    :return : tuple of the string normalissssss and the list normalissssss
    
    """
    
    #Check if the list is empty
    if len(T) == 0:
        return ("",T)
    
        
    #Removing the fucking useless zeros at the end of the list
    j = len(T)-1
    while T[j] == 0:
        j -= 1
        if j == -1:
            break
        T.pop()
    if j==-1:
        return ("",[])
    
    s = ""
    for i in range(len(T)):
        s += "{}x^{} + ".format(T[i],i)
    s = s[:-2]
    return (s,T)
        

    
"""    
# -*- coding: utf-8 -*-

def normalissssss(T):
    j = len(T)-1
    while T[j] == 0:
        j -= 1
        T.pop()
    s = ""
    for i in range(len(T)-1):
        print("{}x^{} + ".format(T[i],i),end="")
    print("{}x^{}".format(T[len(T)-1],len(T)-1))
 
        
if __name__=="__main__":
    normalissssss([1,5,1,5,0,0,0,0,0])
"""

def complex(T):
    s,t = normalissssss(T)
    return len(t)
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    T = [1,5,1,5,0,0,0,0,0]
    c = complex([0,0,0,0,0,0,0,0,0,0,0])
    print(c)