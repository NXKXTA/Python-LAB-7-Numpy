Работа с библиотекой Numpy
Во всех задачах этой темы необходимо использовать механизм исключений для
проверки корректности введённых данных везде, где это возможно.
При решении задач необходимо использовать библиотеку Numpy. Постарайтесь
применить как можно больше возможностей этой библиотеки.

1. Сгенерируйте две матрицы А и B размера N x N (N вводит
   пользователь) и заполните их случайными целыми числами из
   диапазона [1…100]. Выполните поэлементное сравнение
   матриц (a > b, a < b или a == b) и в качестве результата выведите
   на консоль матрицу C, которая состояла бы из булевских
   значений, соответствующих результату поэлементного
   сравнения.
2. Сгенерируйте матрицу А размера Nx N (N вводит пользователь)
   и заполните её случайными целыми числами из диапазона
   [1…100]. Выведите на консоль получившуюся матрицу и номер
   столбца, сумма чисел в котором минимальна
3. Напишите программу для решения системы линейных
   уравнений Ax=b. Размерность системы и коэффициенты
   уравнений считайте из текстового файла.
4. В файле udemy_courses.csv содержатся данные о курсах
   Udemy, о каждом курсе в отдельной строке, где значения
   параметров разделены запятыми. Формат строки следующий:
   название курса, цена, количество подписчиков, количество
   лекций, уровень курса, продолжительность курса.
   Проанализируйте файл и выведите на консоль следующую
   информацию:
   a. Среднюю цену на курс.
   b. Минимальное число подписчиков.
   c. Максимальную продолжительность лекций.
   d. Уровень, для которого было создано наибольшее
   количество курсов (для решения этой задачи вам нужно
   выполнить предобработку данных и перекодировать
   строковые значения в числовые)