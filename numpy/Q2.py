import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
pares = []
print(f"array original = {arr}")
for n in arr:
    if n % 2 == 0:
        pares.append(n)

pares = np.array(pares)
print(f"array só com os pares = {pares}")
