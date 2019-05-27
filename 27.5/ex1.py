import copy
import time

def exo1():
    #1.1
    old = [2, 3, 5, 7]
    new = copy.deepcopy(old)
    new [3] = 8
    print(new)

    #1.2
    old = [2, 3, 5, [7, 11]]
    new = copy.deepcopy(old)
    new [3][0] = 8
    print(new)


class Matrice:
    def __init__(self, valeur):
        self.valeur = valeur

    def type_1(self,h,k,a):
        #Lh <- Lh + aLk

        #Parcours les elements de Lh
        for counter,element in enumerate(self.valeur[h]):
            self.valeur[h][counter] = element + a * self.valeur[k][counter]
            
    def type_2(self,h,a):
        #Lh <- aLh
        for counter,element in enumerate(self.valeur[h]):
            self.valeur[h][counter] = element * a

    def type_3(self,h,k):
        #Lh <-> Lk
        Lk = self.valeur[k]

        #Lh -> Lk
        for counter,element in enumerate(self.valeur[k]):
            self.valeur[k][counter] = self.valeur[h][counter]

        #Lk -> Lh
        for counter,element in enumerate(self.valeur[k]):
            self.valeur[h][counter] = Lk[counter]


    def pivot(self,k):
        valeurs = [abs(self.valeur[i][k]) for i in range(len(self.valeur[k])-1)]
        piv = max(valeurs)
        index = valeurs.index(piv)
        return piv,index


    def Cramer(self):
        nombre_colonne = len(self.valeur[0])
        for i in range(nombre_colonne-1):
            
            piv,index = self.pivot(i)
            valeur_colonne = [self.valeur[i][j] for j in range(nombre_colonne)]

            
                
            #Pivot = 1
            self.type_2(i,1/piv)

            #Detruit
            if i+1 != nombre_colonne:
                for j in range(i+1,nombre_colonne):
                    a = piv*(-self.valeur[j][i] / piv)
                    self.type_1(j,i,a)
            
            
        

    def __str__(self):
        s = ""
        for ligne in self.valeur:
            s += str(ligne)
            s += "\n"
        return s



def generer_identite(n):
    identite = []
    for i in range(n):
        ligne = [0 for j in range(n)]
        ligne[i] = 1
        identite.append(ligne)
    return identite
        

if __name__ == "__main__":
    iden2 = generer_identite(2)
    test = [[2,1],[3,7]]
    t = [[1,1,1,1],[3,3,0,1],[-1,-1,2,1],[0,0,3,2]]
    m = Matrice(t)
    m.Cramer()
    print(m)









