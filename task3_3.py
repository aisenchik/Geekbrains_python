"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    max_1 = max(my_list)
    my_list.remove(max_1)
    max_2 = max(my_list)
    return max_1 + max_2


print(my_func(5, 5, 5))