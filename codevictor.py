#Je créé le programme de représentation des figures

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Création d'un tableau 13x13 avec des nombres
# Par exemple, les valeurs peuvent être comprises entre 0 et 3 pour 4 couleurs
data = np.random.randint(0, 13, size=(13, 13))

# Définition d'une carte de couleurs viridis/ plasma
cmap = plt.cm.get_cmap('plasma', 13)  # 4 couleurs différentes

# Affichage du damier
plt.imshow(data, cmap=cmap, interpolation='nearest')
plt.title('Puzzle')
plt.axis('off')  # Supprime les axes pour une meilleure présentation
plt.show()


