
""" Tracé de nuages de points à partir d'un fichier de mesures

le fichier de données à utiliser est Maxpid.txt
situé dans P:/mathsup/mpsi1/info/TP_trace

"""
import numpy as np  #import de la librairie nupy renomée np
import matplotlib.pyplot as plt # import de la bibliothèque matplotlib renommée np (pour les tracés) 

X= np.loadtxt("I:/Jacques/LK_2015/IPT/maxpid.txt",skiprows=2) #mettre le chemin adapté
t=X[:,0]
position=X[:,2]
tension=X[:,3]

# en plus direct 
# t,position,tension=np.loadtxt("I:/Jacques/LK_2015/IPT/maxpid.txt",usecols=(0,2,3),skiprows=2,unpack=True)

plt.plot(t,position,marker='+',color='r', ls='', label="position[degré]")
plt.plot(t,tension,marker='*',color='g', ls='', label="tension[V]")

plt.legend(loc='center right')  #  a tester comme option dans plt.legend() : loc='center right'
plt.grid(True)
plt.xlabel('temps[ms]')
plt.title("Réponse du système")
plt.show()
