# Matriz A e B (mesmo tamanho: 2x2)
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Adição: Criando matriz C
C_adicao = [[0, 0], [0, 0]]
for i in range(2):  # Linhas
    for j in range(2):  # Colunas
        C_adicao[i][j] = A[i][j] + B[i][j]

print("Adição das matrizes:", C_adicao)

# Subtração: Criando matriz D
D_subtracao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        D_subtracao[i][j] = A[i][j] - B[i][j]

print("Subtração das matrizes (A - B):", D_subtracao)
