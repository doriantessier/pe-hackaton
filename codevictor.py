#Je créé le programme de représentation des figures

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(0, 13, size=(13, 13))

# Types de couleur viridis/ plasma et création du damier
cmap = plt.cm.get_cmap('plasma', 13) 

# Affichage du damier
plt.imshow(data, cmap=cmap, interpolation='nearest')
plt.title('Puzzle')
plt.show()


#on créé l'espace de jeu aka la grille
taillegrille=(7,7)
EDJ=np.zeros(taillegrille)
#on code les tailles sur une taille sur une grille 5x5
p1=np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
liste_piece=[]
def peut_placer(piece,position,EDJ,numero):
    for i in range(len(piece)):
        for j in range (len(piece[0])):
            if piece[i][j]==1:
                if i + position[0] >= len(EDJ) or j + position[1]>=len(EDJ[0]):
                    if EDJ[i + position[0]][j + position[1]]:
                        return False
    return True

def place(piece,position,EDJ,numero):
    for i in range(len(piece)):
        for j in range (len(piece[0])):
            if piece[i][j]==1:
                EDJ[i + position[0]][j + position[1]]=numero

def enleve(piece,position,EDJ,numero):
    for i in range(len(piece)):
        for j in range (len(piece[0])):
            if piece[i][j]==1:
                EDJ[i + position[0]][j + position[1]]=0

"""def resolution(listepiece,EDJ):
    numero=0
    listechoix=[]
    position=[0,0]
    while numero<len(listepiece-1):
        if position[1]=len(EDJ[0]):
            position[0]+=1
        if position[]
        piece=listepiece[numero]
        if """

def symetrieax0(piece):
    symax0piece=piece[:][::-1]
    return symax0piece

def symetrieax1(piece):
    symax1piece=piece[::-1][:]
    return symax1piece

def toutessymetries(piece):
    listesym=[piece]
    listesym.append(symetrieax0(piece))
    listesym.append(symetrieax1(piece))
    listesym.append(symetrieax0(symetrieax1(piece)))
    return listesym