"Mon dossier pour le Hackaton"

import pandas as pd 
import numpy as np
from copy import copy

RAW_SHAPES = {
    "F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    "I": [[1, 1, 1, 1, 1]],
    "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
    "P": [[1, 1, 1], [1, 1, 0]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 1, 1], [1, 0, 1]],
    "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}

#from xcover import covers
#options = [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]
#print(list(covers(options)))

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


def variante(A):
    L=toutessymetries(A)
    F=copy(L)
    for M in L :
        F.append(np.transpose(M))
    return F


print(np.transpose(RAW_SHAPES["F"]))
print(variante(RAW_SHAPES["F"]))