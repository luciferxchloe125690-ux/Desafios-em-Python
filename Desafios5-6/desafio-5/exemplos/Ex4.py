import numpy as np

# Matrizes compatíveis: A (2x3) e E (3x2)
A = np.array([[1, 2, 3], [4, 5, 6]])
E = np.array([[7, 8], [9, 10], [11, 12]])

# Multiplicação: np.dot ou @
F_multi = np.dot(A, E)  # Ou A @ E
print("Multiplicação de matrizes:\n", F_multi)
