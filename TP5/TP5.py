def partie_entiere(p,q):
    """
    Marche que si p et q sont positifs
    
    if p<q:
        return 0
    if p >= q and p < 2*q:
        return 1
    return partie_entiere(p-q,q) + 1"""

    
    return p // q #Marche tjrs
    


def test_partie_entiere():
    t = [[1,3],[0,4],[3,3],[7,3],[50,5],[-1,2]]
    for element in t:
        print("Partie entiere de {}/{} = {}".format(element[0],element[1],partie_entiere(element[0],element[1])))

def n_premieres_decimales(p,q,n):
    #String stocke la string que l'on retourne a la fin avec les n premieres decimales
    #Ajoute la partie entiere et la virgule a la string
    string = "{},".format(partie_entiere(p,q))
    #Enleve la partie entiere du nombre pour avoir p/q compris entre 0 et 1
    p -= q*partie_entiere(p,q)
    #Boucle tournant n fois calculer une decimale a chaque fois
    for i in range(n):
        #Principe de la division euclidienne d'un nombre < 1
        p *= 10
        #Ajoute la decimale calculer avec la division euclidienne a la string
        string += str(partie_entiere(p,q))
        #Cacule de la difference entre le numerateur et le produit du denominateur et de la decimale calculer
        p -= partie_entiere(p,q)*q
    return string

def test_n_premieres_decimales():
    t = [[1,3],[0,4],[3,3],[7,3],[50,5],[-1,2]]
    for element in t:
        print("Les n premieres decimales {} et {} sont : {}".format(element[0],element[1],n_premieres_decimales(element[0],element[1],100)))


def partie_periodique(p,q):
    #Pas fini
    p -= q*partie_entiere(p,q)
    R = []
    string = ""
    rest = 0
    last_p = p
    while rest not in R:
        rest = partie_entiere(last_p,q)
        p *= 10
        R.append(partie_entiere(p,q))
        string += str(partie_entiere(p,q))
        last_p = p
        p -= partie_entiere(p,q)*q
    return string

def test_partie_periodique():
    t = [[1,3]]
    for element in t:
        print(partie_periodique(element[0],element[1]))
    
if __name__ == "__main__":
    test_partie_periodique()
