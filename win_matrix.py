import numpy as np

m = np.array([
    [-1, -4, 5],
    [-2, 3, -3],
    [-5, -3, 3]
])

alpha = 1
p = np.array([1/2, 1/4, 1/4])

wald = np.argmax(np.min(m, axis=1))
savage = np.argmin(np.max(np.max(m, axis=0) - m, axis=1))
hurwicz = np.argmax(alpha * np.max(m, axis=1) + (1 - alpha) * np.min(m, axis=1))
bayes = np.argmax(np.sum(m * p, axis=1))
maximax = np.argmax(np.max(m, axis=1))

print(f"Вальда: {wald + 1}")
print(f"Сэвиджа: {savage + 1}")
print(f"Гурвица: {hurwicz + 1}")
print(f"Байеса: {bayes + 1}")
print(f"Максимакс: {maximax + 1}")