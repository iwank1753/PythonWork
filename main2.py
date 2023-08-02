# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def generate_arithmetic_progression():
#     a1 = int(input("Введите первый элемент прогрессии: "))
#     d = int(input("Введите разность прогрессии: "))
#     n = int(input("Введите количество элементов прогрессии: "))

#     progression = [a1 + (i - 1) * d for i in range(1, n + 1)]

#     return progression

# result = generate_arithmetic_progression()
# print("Арифметическая прогрессия:", result)


# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# def find_elements_in_range(arr, min_value, max_value):
#     indices = []
#     for i in range(len(arr)):
#         if min_value <= arr[i] <= max_value:
#             indices.append(i)
#     return indices

# # Пример использования
# arr = [2, 5, 8, 11, 14]
# min_value = 4
# max_value = 10
# result_indices = find_elements_in_range(arr, min_value, max_value)
# print("Индексы элементов, принадлежащих заданному диапазону:", result_indices)

