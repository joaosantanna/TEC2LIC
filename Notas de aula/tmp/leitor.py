nome = []
notas = []
texto = []
with open("nomes.txt", "r") as arq:
    texto = arq.readlines()
    for linha in texto:
        print(linha, end="")
    print(texto)

for item in texto:
    tmp = item.split(":")
    nome.append(tmp[0])
    notas.append(float(tmp[1]))

print(nome)
print(notas)
