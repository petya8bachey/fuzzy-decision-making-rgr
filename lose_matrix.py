import numpy as np

m = np.array([
    [-1, -4, 5],
    [-2, 3, -3],
    [-5, -3, 3]
])

alpha = 1
p = np.array([1/2, 1/4, 1/4])

wald = np.argmin(np.min(m, axis=1))
savage = np.argmin(np.max(m - np.min(m, axis=0), axis=1))
hurwicz = np.argmin(alpha * np.min(m, axis=1) + (1 - alpha) * np.max(m, axis=1))
bayes = np.argmin(np.sum(m * p, axis=1))
minimin = np.argmin(np.min(m, axis=1))

print(f"Вальда: {wald + 1}")
print(f"Сэвиджа: {savage + 1}")
print(f"Гурвица: {hurwicz + 1}")
print(f"Байеса: {bayes + 1}")
print(f"Минимин: {minimin + 1}")