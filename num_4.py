import csv
import numpy as np

# Загрузка данных из CSV-файла
try:
    with open("udemy_courses.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        courses_data = list(reader)
except FileNotFoundError:
    print("Файл с курсами не найден!")
    exit()

for i in range(1, len(courses_data)):
    courses_data[i][1] = int(courses_data[i][1])
    courses_data[i][2] = int(courses_data[i][2])
    courses_data[i][3] = int(courses_data[i][3])
    courses_data[i][-1] = float(courses_data[i][-1])

# Преобразование списка в numpy-массив
courses_data_np = np.array(courses_data)

# Расчет средней цены курса
average_price = sum(int(i[1]) for i in courses_data[1:]) / len(courses_data[1:])
# avg_price = np.mean(courses_data_np[1:, 1])

# Поиск курса с минимальным числом подписчиков
# min_students_idx = np.argmin(courses_data_np[1:, 2])  # Индекс курса с минимальным количеством подписчиков
# min_students_course = courses_data_np[min_students_idx][0]  # Название курса с минимальным количеством подписчиков
# min_students = courses_data_np[min_students_idx][2]  # Минимальное количество подписчиков
min_students = min(int(i) for i in courses_data_np[1:, 2])

# Поиск курса с максимальной продолжительностью лекций
# max_duration_idx = np.argmax(courses_data_np[1:, -1])  # Индекс курса с максимальной продолжительностью
# max_duration_course = courses_data_np[max_duration_idx][0]  # Название курса с максимальной продолжительностью
# max_duration = courses_data_np[max_duration_idx][-1] # Продолжительность курса с максимальной продолжительностью
max_duration = max(float(i) for i in courses_data_np[1:, -1])

# print(set([i for i in courses_data_np[1:, -2]]))  # Вывод уровней сложности
# Преобразование уровней в числовые значения
levels_map = {"All Levels": 0, "Beginner Level": 1, "Intermediate Level": 2, "Expert Level": 3}
numerical_array = np.vectorize(levels_map.get)(courses_data_np[1:, -2])
# Подсчет количества каждого элемента
element_counts = np.bincount(numerical_array)
# Поиск индекса наиболее часто встречаемого элемента
most_frequent_index = np.argmax(element_counts)
# Берём элемент с наиболее часто встречаемым значением
most_frequent_element = numerical_array[most_frequent_index]
count = element_counts[most_frequent_index]
for level, level_value in levels_map.items():
    if most_frequent_element == level_value:
        most_frequent_element = level
        break

print(f"Средняя цена курса: {average_price}")
print(f"Минимальное количество подписчиков: {min_students}")
print(f"Максимальная продолжительность курса: {max_duration}")
print(f"Самый часто встречаемый уровень сложности: {most_frequent_element} (Количество таких курсов: {count})")
