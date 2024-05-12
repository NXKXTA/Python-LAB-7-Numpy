import numpy as np

try:
    # Ввод размера матриц
    n = int(input("Введите размер матриц (N x N): "))

    # Проверка корректности введенного значения
    if n <= 0:
        raise ValueError("Размер матриц должен быть больше 0")
except ValueError as err:
    print(f"Ошибка: {err}")
    exit()

# Генерация матриц A и B
A = np.random.randint(1, 101, size=(n, n))
B = np.random.randint(1, 101, size=(n, n))
print(A)
print(B)

# Поэлементное сравнение матриц
C = A > B
C = np.logical_or(C, A < B)
C = np.logical_or(C, A == B)

# Вывод матрицы C
print("Матрица C:")
print(C)
