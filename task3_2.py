"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_profile(first_name, last_name, year, city, email, phone):
    print(first_name, last_name, year, city, email, phone)


user_profile(first_name='Alexey',
             last_name='Borisov',
             year=1992,
             city='Moscow',
             email='example@mail.ru',
             phone=8800800800)