import numpy as np
from faker import Faker
from beautifultable import BeautifulTable

table = BeautifulTable()
f = Faker("pt_BR")

nomes = []
for i in range(50):
    nomes.append(f.name())

nota = np.random.randint(40, 100, size=(50, 3))  # menor nota 4 maior 10


for i in range(50):
    table.append_row([nomes[i], nota[i, 0], nota[i, 1], nota[i, 2]])

table.columns.header = ["Nome", "1NAP", "2NAP", "Subs"]
table.columns.alignment["Nome"] = BeautifulTable.ALIGN_LEFT
print(table)

primeira_ava = nota[:, 0]
media_calculada = np.sum(primeira_ava) / 50

print(f"Media da primeira avaliação = {np.mean(nota,axis=0)}")
print(f"media calculada = {media_calculada}")

media = np.mean(nota)

print(f"Media geral = {media}")
print("todas as notas acima da media geral")
print(nota[np.where(nota > media)])
