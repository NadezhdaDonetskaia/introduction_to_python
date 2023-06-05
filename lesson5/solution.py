from icecream import ic
# Задача:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def get_degree(num, degree):
    if degree == 0:
        return 1
    if degree == 1:
        return num
    return num * get_degree(num, degree - 1)

ic(get_degree(3, 5))
ic(get_degree(2, 3))

# Задача: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def _sum(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 1:
        return 1 + _sum(0, b)
    if b == 1:
        return 1 + _sum(a, 0)
    if a > 1:
        return 1 + _sum(a - 1, b)
    return 1 + _sum(a, b - 1)

ic(_sum(2, 2))
ic(_sum(0, 0))
ic(_sum(1, 0))
ic(_sum(0, 1))
ic(_sum(3, 5))
