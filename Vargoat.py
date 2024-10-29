"Mon dossier pour le Hackaton"

import pandas as pd 
import numpy as np

from xcover import covers
options = [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]
print(list(covers(options)))  #test

def variante(A):
    L=toutessymettries
    F=copy(L)
    for M in L :
        F.append(np.transpose(M))
    return F


