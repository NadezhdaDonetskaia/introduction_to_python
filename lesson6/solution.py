from icecream import ic

# Задача:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(firs_el, step, len_progression):
    return [firs_el + step * i for i in range(len_progression)]

f_el = int(input('Введите первый элемент: '))
step = int(input('Введите шаг прогрессии: '))
pr_len = int(input('Введите длину прогрессии: '))

ic(arithmetic_progression(f_el, step, pr_len))

# Задача: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def get_index(lst, min, max):
    range_nums = range(min, max + 1)
    result = []
    for i, el in enumerate(lst):
        if el in range_nums:
            result.append(i)

    return result

l = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
ic(get_index(l, 3, 10))
