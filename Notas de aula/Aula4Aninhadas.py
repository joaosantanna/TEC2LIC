turma = [
    {"nome": "Danilo", "nota 1": 8, "nota 2": 7.5, "nota 3": 9},
    {"nome": "Kelren", "nota 1": 9.5, "nota 2": 8, "nota 3": 10},
    {"nome": "Joao Victor", "nota 1": 10, "nota 2": 9.5, "nota 3": 7},
]

soma1 = 0
soma2 = 0
soma3 = 0
for aluno in turma:
    soma1 += aluno["nota 1"]
    soma2 += aluno["nota 2"]
    soma3 += aluno["nota 3"]


print(f"Media da primeira avaliação = {soma1/3:.2f}")
print(f"Media da segunda avaliação = {soma2/3:.2f}")
print(f"Media da terceira avaliação = {soma3/3:.2f}")
