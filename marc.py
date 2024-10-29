import numpy as np

def rotate(piece):
    L = []
    for i in range(4):
        nouvelle_piece = np.rot90(piece, k=-i)
        L.append(nouvelle_piece)
    return L


def reflect(piece):
    return np.flip(piece, axis=1)


import matplotlib.pyplot as plt
import numpy as np

def plot_solution(solution, board_shape, obstacles=None, colormap='viridis'):
    """Affiche la solution à l'aide de matplotlib."""
    # Préparer le tableau de visualisation
    output = np.zeros(board_shape, dtype=int)
    
    # Remplir le tableau avec les indices des pièces
    for piece_index, positions in enumerate(solution):
        for pos in positions:
            row = pos // board_shape[1]
            col = pos % board_shape[1]
            output[row, col] = piece_index + 1  # Utiliser un index basé sur 1 pour les pièces

    # Si des obstacles sont fournis, les ajouter au tableau de visualisation
    if obstacles is not None:
        output[obstacles == 1] = 0  # Garder les obstacles comme 0

    # Créer la figure
    plt.figure(figsize=(8, 8))
    plt.imshow(output, cmap=colormap, alpha=1.0)
    
    # Personnaliser l'affichage
    plt.colorbar(ticks=np.arange(0, len(solution) + 1))
    plt.title("Solution des Pentominos")
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)

    # Afficher l'image
    plt.show()

plot_solution(solution, board_shape, obstacles, colormap='viridis')