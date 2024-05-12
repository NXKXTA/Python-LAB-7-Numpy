import numpy as np

file_path = "./1.txt"


def read_system_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

            # Извлечение размерности системы
            n = int(lines[0].strip())
            m = int(lines[1].strip())
            # Проверка размерности
            if n <= 0 or m <= 0:
                raise ValueError("Размерность системы должна быть больше 0")

            # Инициализация матрицы A и вектора b
            A = np.zeros((n, m))
            b = np.zeros(n)

            # Заполнение матрицы A и вектора b данными из файла
            for i, line in enumerate(lines[2:-1]):
                row_data = line.strip().split()
                for j, value in enumerate(row_data):
                    A[i, j] = float(value)

            row_data = lines[-1].strip().split()
            for i, value in enumerate(row_data):
                b[i] = float(row_data[i])

        return A, b
    except (FileNotFoundError, ValueError) as err:
        print(f"Ошибка: {err}")
        exit()


def solve_system(A, b):
    """
    Args:
        A (ndarray): Матрица коэффициентов системы.
        b (ndarray): Вектор правых частей системы.

    Returns:
        ndarray: Вектор решения системы x.
    """
    try:
        # Решение системы с помощью Numpy.linalg.solve
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        print("Система линейных уравнений не имеет решения.")
        return None


# Чтение системы из файла
A, b = read_system_from_file(file_path)

# Решение системы
x = solve_system(A, b)

# Вывод решения
if x is not None:
    print(f"Решение системы:")
    print(x)
else:
    print("Система не имеет решения.")
