import numpy as np

try:
    # Ввод размера матрицы
    n = int(input("Введите размер матрицы (N x N): "))

    # Проверка корректности введенного значения
    if n <= 0:
        raise ValueError("Размер матрицы должен быть больше 0")
except ValueError as err:
    print(f"Ошибка: {err}")
    exit()

# Генерация матрицы A
A = np.random.randint(1, 101, size=(n, n))

# Вывод матрицы A
print(f"Матрица A:\n{A}")

# Поиск столбца с минимальной суммой
column_sum = np.sum(A, axis=0)  # Суммы элементов каждого столбца. (axis=1) находит сумму строк
index_of_column_with_min_sum = np.argmin(column_sum)  # Индекс столбца с мин. суммой

# Вывод суммы и индекса столбца с минимальной суммой
print(f"Номер столбца с минимальной суммой: {index_of_column_with_min_sum + 1}")
print(f"Минимальная сумма: {column_sum[index_of_column_with_min_sum]}")
