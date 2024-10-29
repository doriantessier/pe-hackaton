import numpy as np

# Dictionnaire de formes de pentominos (matrices)
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

def convert_shape_to_coordinates(shape):
    """
    Convertit une matrice de 0 et 1 en une liste de coordonnées (r, c) pour chaque cellule de la pièce.
    
    Arguments :
    - shape : liste de listes représentant la forme de la pièce (matrice de 0 et 1)
    
    Retourne :
    - Liste de tuples (r, c) représentant les positions de la pièce
    """
    coordinates = []
    for r, row in enumerate(shape):
        for c, val in enumerate(row):
            if val == 1:
                coordinates.append((r, c))
    return np.array(coordinates)

# Génération de la liste des pièces avec index et coordonnées
pentomino_list = [(idx, convert_shape_to_coordinates(shape)) for idx, shape in enumerate(RAW_SHAPES.values())]

# Fonction déjà définie
def generate_pentomino_positions(pentomino_idx, pentomino_shape, grid_shape=(6, 10)):
    """
    Génère toutes les positions possibles d'un pentomino sur une grille et renvoie un tableau de 0 et 1
    où chaque ligne correspond à une configuration possible.
    
    Arguments :
    - pentomino_idx : l'index de la pièce choisie (de 0 à 11 pour les 12 pentominos).
    - pentomino_shape : un array numpy de forme (5, 2) représentant les coordonnées des 5 cases de la pièce.
    - grid_shape : la taille de la grille (6, 10) par défaut pour une grille de 60 cases.
    
    Retourne :
    - Un array numpy avec autant de lignes que de positions possibles et 72 colonnes par ligne.
    """
    
    possible_positions = []
    rows, cols = grid_shape
    
    for row_offset in range(rows):
        for col_offset in range(cols):
            position = []
            valid_position = True
            for (r, c) in pentomino_shape:
                new_row = row_offset + r
                new_col = col_offset + c
                if new_row >= rows or new_col >= cols:
                    valid_position = False
                    break
                position.append((new_row, new_col))
            
            if valid_position:
                row = np.zeros(72, dtype=int)
                row[pentomino_idx] = 1
                
                for (r, c) in position:
                    index_in_grid = r * cols + c
                    row[12 + index_in_grid] = 1
                
                possible_positions.append(row)
    
    return np.array(possible_positions)

# Générer toutes les positions pour les 12 pièces
def generate_all_pentomino_positions(pentomino_list, grid_shape=(6, 10)):
    all_positions = []
    for pentomino_idx, pentomino_shape in pentomino_list:
        positions = generate_pentomino_positions(pentomino_idx, pentomino_shape, grid_shape)
        all_positions.append(positions)
    
    return np.vstack(all_positions)

# Génération des configurations pour toutes les pièces
output = generate_all_pentomino_positions(pentomino_list)

# Afficher la forme du résultat
print(output.shape)  # Affichera (nombre_total_de_positions, 72)
print(output[:5])  # Afficher les 5 premières configurations pour vérification
