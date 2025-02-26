import numpy as np

mat = np.random.randint(1, 100, size=(5, 5))
print(mat)
maior = np.max(mat, axis=1)  # axis 1 - por linha
print(f" maiores numeros por linha = {maior}")

media = np.mean(mat, axis=0)  # axis 0 - por coluna
print(f"Media dos numeros por coluna = {media}")

# mat.sort() # o sort do numpy ordena os numeros nas suas
# print(mat) # respectivas linhas
valores = mat.copy()
valores = np.ravel(valores)
valores.sort()
valores.shape = (5, 5)
print(valores)

print(mat)
print(" maiores que 50 agora sao 0")
mat[np.where(mat > 50)] = 0
print(mat)
