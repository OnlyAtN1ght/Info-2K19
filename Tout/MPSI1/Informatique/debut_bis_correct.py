

""" Ceci est le début du programme de promenade dans un labyrinthe
Les murs sont faits du caractère "X"
L'entrée est repérée "E" sur le contour
La sortie est repérée "S" sur le contour

Rappel des fonctions à construire:

TrouverEntree() : doit retourner l'index de l'entrée

ListePossibles(i): doit retourner la liste des indices possibles
(tout sauf mur)

EvolutionLabyrinthe(L,i):  retourne une chaine de caractères
qui est le labyrinthe L avec un "o" à l'indice i

"""

from random import randint  # on importe du module random uniquement randint


""" fonctions utiles:
 on voit le labyrinthe comme un tableau avec l lignes entre 0 et l-1
 et c colonnes entre 0 et c-1
 une case  est repérée par :
      son indice de ligne  
      son indice de colonne      
"""

def IndiceLigCol(i):
    # retourne  un tuple comprenant l'ndice de ligne et l'indice de colonne.
    # Attention: les indices i*(c+1) correspondent à \n qui n'est pas dans
    # le tableau; IndexLigCol(k*47) retourne k-1 ,46  dans lequel 46 est hors
    # tableau; on ne doit pas demander IndiceLigCol(k*(c+1))
    lig= (i-1)//(c+1)
    col= (i-1)% (c+1)
    return lig ,col


def LigColIndice(lig,col):
    # retourne l'indice correspondant à la case
    # aucune verification n'est faite de la validité de lig et col
    # 0<= lig < l  et  0<= col < c
    
    return 1+lig*(c+1)+col


def FaceEntree():
    # donne la face sur laquelle on entre :"Nord" "Ouest" "Sud" "Est"
    # servira si on veut longer un mur.
    lig,col=IndiceLigCol(iEntree)
    if   col==0 :
        return "Ouest"
    elif col==c-1 :
        return "Est"
    elif lig==0 :
        return "Nord"
    else :
        return "Sud"


def ListePossibles(i):
    # retourne la liste des indices des cases voisines  et accessibles de l'indice
    Voisins=[]
    il,ic= IndiceLigCol(i)
    if  ic < c-1 :
        if Laby[i+1] !='X' :
            Voisins.append(i+1)
    if  ic > 0    :
        if Laby[i-1] !='X' :
            Voisins.append(i-1)
    if il < l-1 :
        if Laby[i+c+1] !='X' :
            Voisins.append(i+c+1)
    if il > 0 :
        if Laby[i-(c+1)] !='X' :
            Voisins.append(i-(c+1))        
    return Voisins

#-------------------------------------------------------------------------
def EvolutionLabyrinthe(L,i):
    # retourne UN labyrinthe  qui est le labyrinthe L avec une trace de la position i:
    L= L[0:i]+'o'+L[i+1:]
    return L

#-------------------------------------------------------------------------
# deplacement aleatoire (on peut revenir en arrière)
def Divague(L,i):
    # renvoie l'indice de la prochaine position
    # A faire
    return(" ")    

#--------------------------------------------
Laby1="""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXX                                   X    E
XXXXX XXXXXXXXXXXXXXXXXXXXX XXX XXXXXXX X XXXX
S     XXXXXX                  X XXXXXXXXX    X
X XXX     XX XXX XXX XXXXXX XXX X       XXXX X
X   X XXXX X XXX XXX XXXXXX XXX X XXXXX XXXX X
XXXXX XXXX X             XX     X XXX X XXXX X
XX XXXX XXXXX XXXXXXXXXXXXXXXXXXX     X XXXX X
XXX   X XX             XXXX       XXXXX      X
XXX X X XX XXXXXXXXXXX XXXX XXXXXXXXXXXXXXXXXX
XXX X   XX XXX XXXXXXX XXXX              X   X
XXX X XXXX          XX XXXX XXXXXXXXXXXX X X X
XXX X XXXXXXXX XXX XXX XXXX XXXXXXXXX XX XXX X
XXXXX          XXXXXXX                XX     X
XXX XXX X XXXXXXXXXXXXXXXXXXX XX XXXXXX XXXXXX
XXX     X                     XX        XXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

Laby0="""
XXXXXXXXXX
X        X
X XXXXXX E
S X      X
X XXXXXXXX
X        X
XXXXXXXXXX
"""

LTest="""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXX                                   X    E
XXXXX XXXXXXXXXXXXXXXXXXXXX XXX XXXXXXX X XXXX
S     XXXXXX                  X XXXXXXXXX    X
X XXX     XX XXX XXX XXXXXX XXX X       XXXX X
X   X XXXX X XXX XXX XXXXXX XXX X XXXXX XXXX X
XXXXX XXXX X             XX     X XXX X XXXX X
XX XXXX XXXXX XXXXXXXXXXXXXXXXXXX     X XXXX X
XXX   X XX   A         XXXX       XXXXX      X
XXX X X XX XXXXXXXXXXX XXXX XXXXXXXXXXXXXXXXXX
XXX X   XX XXX XXXXXXX XXXXB             X   X
XXX X XXXX          XX XXXX XXXXXXXXXXXX X X X
XXX X XXXXXXXX XXX XXX XXXX XXXXXXXXX XX XXX X
XXXXX          XXXXXXX                XX     X
XXX XXX XCXXXXXXXXXXXXXXXXXXX XX XXXXXX XXXXXX
XXX     X                     XX       DXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""


# ICI commence la partie principale du programme
# qui utilise les fonctions définies prcédemment:

# ON CHOISIT LE LABYRINTHE SUR LEQUEL ON VA TRAVAILLER:
Laby=LTest


#-------------------------------------------------------------
# nombre de lignes: l
# compter le nombre de \n : il y en a 1 de plus que de lignes
l=0
for car in Laby:
    if car=='\n' : l+=1
l-=1
print("nombre de lignes du tableau: ",l)

#-------------------------------------------------------------

# nombre de colonnes: c
c=(len(Laby)-1)//l -1
print("nombre de colonnes du tableau (y compris \\n ):", c)
#-------------------------------------------------------------

#indice de l'entrée: iEntree
trouve=False
i=0
# il y a obligatoirement une entrée donc pas de précaution
while not trouve:
    if Laby[i]=='E' :
        trouve=True
    else : i+=1

iEntree=i
print("indice de l'entrée:",iEntree)
#--------------------------------------------------------------

# Quelques pas aléatoires dans le labyrinthe:


Npas=20
Historique=[iEntree]  # une liste pour suivre les mouvements qui commence à l'entrée
                        # la case courante est le dernier élément de Historique

for i in range(Npas+1):
    Liste=ListePossibles(Historique[i])
    NouvPos=93  #  A MODIFIER POUR NE PAS FAIRE DU SURPLACE A L'ENTREE
    Laby=EvolutionLabyrinthe(Laby,NouvPos)# on modifie Laby
    Historique.append(NouvPos); # on ajoute la nouvelle position à l'historique


print(Laby)
print(Historique)

def aléa(N,i):
	Historique=[i]
	L=Laby1
	for k in range(N+1):
		Liste=ListePossibles(Historique[k])
		h=randint(0,len(Liste)-1)
		if len(Liste)>1 and L[h]==Liste[-1]:
			Liste.remove(L[h])
		h=randint(0,len(Liste)-1)
		NouvPos=Liste[h]
		L=EvolutionLabyrinthe(L,NouvPos)
		Historique.append(NouvPos)
	L=L[0:NouvPos]+'F'+L[NouvPos+1:]
	print(L)
	print(Historique)


	
