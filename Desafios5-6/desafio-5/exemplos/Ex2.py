from Ex1 import notas

# Acessando um elemento
print("Nota do Aluno 1 na disciplina 2:", notas[0][1])

# Modificando um elemento
notas[1][2] = 9.0  # Atualiza nota do Aluno 2 na disciplina 3
print("Matriz atualizada:", notas)

# Calculando média do Aluno 1
media_aluno1 = (notas[0][0] + notas[0][1] + notas[0][2]) / 3
print("Média do Aluno 1:", media_aluno1)
