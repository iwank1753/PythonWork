# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# def count_vowels(word):
#     vowels = "aeiouаеёиоуыэюя"  # список гласных букв
#     return sum(1 for letter in word if letter.lower() in vowels)

# def check_rhythm(poem):
#     lines = poem.split()  # разделяем стихотворение на фразы
#     syllables = []  # список числа слогов в каждой фразе

#     for line in lines:
#         words = line.split("-")  # разделяем фразу на слова
#         total_syllables = sum(count_vowels(word) for word in words)
#         syllables.append(total_syllables)

#     if all(s == syllables[0] for s in syllables):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# # Ввод стихотворения от Винни-Пуха
# poem_input = input("Введите стихотворение Винни-Пуха: ")
# result = check_rhythm(poem_input)
# print(result)

#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print("Operation Table:")
    
#     # Вывод заголовка с номерами столбцов
#     header = "\t"
#     for col in range(1, num_columns + 1):
#         header += f"{col}\t"
#     print(header)
    
#     # Вывод строк таблицы
#     for row in range(1, num_rows + 1):
#         row_values = [str(operation(row, col)) for col in range(1, num_columns + 1)]
#         row_str = f"{row}\t{'\t'.join(row_values)}"
#         print(row_str)

# # Пример: вывод таблицы умножения
# print_operation_table(lambda x, y: x * y)
