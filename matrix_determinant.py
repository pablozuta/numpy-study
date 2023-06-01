import numpy as np 

# define a 3x3 matrix
matrix = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]])

matrix2 = np.array([[2, 1, 3],
    [0, -1, 4],
    [1, 2, -1]])

# calculate the determinant of the matrix
determinant = np.linalg.det(matrix)
determinant2 = np.linalg.det(matrix2)

# mostrar el resultado
print("Determinant: ", determinant)
print("Determinant Matrix 2: ", determinant2)