nome = ["Joao", "Ana", "Pedro", "Maria"]
notas = [7.5, 9.2, 6.75, 8.5]

with open("nomes.txt", "w") as arq:
    for i in range(len(notas)):
        arq.write(nome[i] + ":" + str(notas[i]) + "\n")

print("Arquivo criado com sucesso")
