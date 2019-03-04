def u():
    """
    Exercice 5
    """
    u = 9
    c = [1]
    avant_neuf = [0]
    for i in range(10):
        u = 4*(u**3) + 3*(u**4)
        """
          Question 1)
          Le nombre de 9 terminant les nombres de la suite (un)
          croit comme 2**n
        """
        c.append(nombre_de_neuf(u))
        """
        Question 2)
          Le nombre avant la suite de 9 est 5
        """
        avant_neuf.append(chiffre_avant_neuf(u))
    print(avant_neuf)



def nombre_de_neuf(k):
    """"
    Exercice 5 Q°)1
    """
    nombre_de_neuf = 0
    for element in str(k)[::-1]:
        if element == "9":
            nombre_de_neuf += 1
        else:
            break
    return nombre_de_neuf



def chiffre_avant_neuf(k):
    """
    Exercice 5 Q°)2
    """
    for element in str(k)[::-1]:
        if element != "9":
            return int(element)
    return 0

def test_chiffre_avant_neuf():
    print(chiffre_avant_neuf(99))
    print(chiffre_avant_neuf(19299))
    print(chiffre_avant_neuf(1))
    print(chiffre_avant_neuf(18800099))


def test_nombre_de_neuf():
    print(nombre_de_neuf(99))
    print(nombre_de_neuf(1))
    print(nombre_de_neuf(19111999))




if __name__=="__main__":
    u()
