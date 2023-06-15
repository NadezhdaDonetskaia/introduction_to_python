from icecream import ic
from collections import Counter
# Задача:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

def rhythm_of_poem():
    poem = input('введите стих, Винни: ')
    phrases = poem.split()
    count_vowels = []

    def count_vowels_in_phrase(phrase):
        result = 0
        coutn_letters = Counter(phrase)
        for letter, count in coutn_letters.items():
            if letter in vowels:
                result += count
        return result
    
    for phrase in phrases:
        count_vowels.append(count_vowels_in_phrase(phrase))
    return 'Парам пам-пам' if len(set(count_vowels)) == 1 else 'Пам парам'


# ic(rhythm_of_poem())


# Задача: 
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def print_operation_table(operation, num_rows=6, num_columns=6):
    result = []
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=' ')
            row.append(operation(i, j))
        result.append(row)
        print()
ic(print_operation_table(lambda x, y: x * y))
ic(print_operation_table(lambda x, y: x ** y))
ic(print_operation_table(lambda x, y: x * y, 2, 8))