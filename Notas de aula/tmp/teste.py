from random import randint

valores = dict()
# inicializa dicionario com 0
for i in range(1, 11):
    valores[i] = 0
print(valores)

for i in range(100):
    n = randint(1, 10)
    valores[n] += 1

print(valores)
# porcentagem de sorteios de numeros
for chave, valor in valores.items():
    # chave aqui equivale ao numero sorteado
    print(f"{chave}: {valor:.2f}%")
