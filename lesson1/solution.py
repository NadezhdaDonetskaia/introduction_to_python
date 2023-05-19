# Урок 1. Ввод-Вывод, операторы ветвления
# Задача: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = input('Введите трезначное число: ')


def sum_num(num):
    return sum([int(x) for x in num])


print(f'Сумма цифр трехзначного числа {n} = {sum_num(n)}')

# Задача: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = input('Введите количество всех журавликов: ')
third_part = int(S) // 3
print(f'Катя сделала {third_part * 2} журавликов\n'
      f'Петя и Сережа сделали по {third_part // 2} журавликов')


# Задача: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

#
ticket_num = input('Введите номер билета: ')

print("yes" if sum_num(ticket_num[:3]) == sum_num(ticket_num[3:]) else "no")

# Задача: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n, m, k = input('Введите ширину, длину и  количество долек через пробел: ').split(' ')
n, m, k = int(n), int(m), int(k)

# предполагаем, что если долек столько же, сколько и сама шоколадка, то ОТЛОМИТЬ нельзя
if n * m <= k or k == 0:
    print('no')
elif k % n == 0 or k % m == 0:
    print('yes')
else:
    print('no')