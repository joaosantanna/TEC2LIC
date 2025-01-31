from random import randint

l1 = []
l2 = []

for i in range(10):
    l1.append(randint(1, 10))
    l2.append(randint(1, 10))

print(l1)
print(l2)

lista_iguais = []

s = set(l1).intersection(l2)
lista_iguais = list(s)
print(lista_iguais)
