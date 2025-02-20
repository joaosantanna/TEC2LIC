from random import randint

mat1 = []
mat2 = []

for linha in range(3):
    tmp = []
    for coluna in range(3):
        tmp.append(randint(1, 50))
    mat1.append(tmp)

for linha in range(3):
    tmp = []
    for coluna in range(3):
        tmp.append(randint(1, 50))
    mat2.append(tmp)

# imprimir matriz
print("mat 1")
for linha in mat1:
    print(linha)

print("mat 2")
for linha in mat2:
    print(linha)

# soma matricial
mat3 = []
for linha in range(3):
    tmp = []
    for coluna in range(3):
        tmp.append(mat1[linha][coluna] + mat2[linha][coluna])
    mat3.append(tmp)

print("mat 3")
for linha in mat3:
    print(linha)

# calculando a matriz transposta de mat3
mat4 = []
for linha in range(3):
    tmp = []
    for coluna in range(3):
        tmp.append(mat3[coluna][linha])
    mat4.append(tmp)

print("Transposta de mat3")
for linha in mat4:
    print(linha)

print(f"maior numero da matriz 4 = {max(mat4)}")
