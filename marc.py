import numpy as np

F = np.array([[1, 1, 0], 
              [0, 1, 1], 
              [0, 1, 0]], dtype=int)



def rotate(piece):
    """Rotate the piece 90 degrees clockwise."""
    L = []
    for i in range(4):
        nouvelle_piece = np.rot90(piece, k=-i)
        L.append(nouvelle_piece)
    return L


def reflect(piece):
    """Reflect the piece horizontally."""
    return np.flip(piece, axis=1)

