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


