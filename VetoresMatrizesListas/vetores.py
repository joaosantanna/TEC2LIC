vet1 = [1, 2, 3]
vet2 = [2, 3, 4]

# soma de vetores
vet3 = []
for i in range(3):
    vet3.append(vet1[i] + vet2[i])

print(vet1)
print(vet2)
print(vet3)

# multiplicação de vetor por um escalar
k = 4
vet4 = []
for n in vet1:
    vet4.append(k * n)

print(vet4)

from array import array
from random import randint

vet1 = array("i", [])
for i in range(20):
    vet1.append(randint(1, 100))
print(vet1)

vet2 = array("f", [])
for i in range(20):
    vet2.append(randint(1, 100) / 10)

vet2.append(5)
vet1.append(4.56)
print(vet2)
print(vet1)
