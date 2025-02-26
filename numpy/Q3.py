import numpy as np

a = np.random.rand(3, 3)
print(f"Matriz a: \n {a}")
b = np.random.rand(3, 3)
print(f"Matriz b: \n {b}")

c = a * b
print(f"Matriz resultado apos multiplicação: \n {c}")

d = a.dot(b)
print(f"Multiplicacao matricial a x b = \n {d}")

e = a + b
print(f"Soma a + b = \n {e}")
