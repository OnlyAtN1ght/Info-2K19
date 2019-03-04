import matplotlib.pyplot as plt
import numpy as np



def suite(x,n,plot=True):
	"""
	Exercice 3 Q°)1
	"""
	Y = [x]

	#Calcule les termes de la suite xn
	for i in range(n):
		x = (x**2)/(i+1)
		Y.append(x)
		
	if plot:
		#Afficeh les valeurs de x dans un graphe
		X = [i for i in range(len(Y))]
		plt.plot(X,Y)
		plt.ylabel('valeur de la suite')
		plt.xlabel("n")
		
		
	return x

def test():
	"""
	Q°) 2
	"""
	#Suite tend vers 0
	suite(1.6616,31)
	#Suite tend vers + l'infini
	suite(1.6617,17)
	   
	plt.show()
	

if __name__=="__main__":
	test()

					
