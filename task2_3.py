'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

# 1-е решение через списки

winter = [12, 1, 2]
summer = [6, 7, 8]
autumn = [9, 10, 11]
spring = [3, 4, 5]

user_month = int(input('Введите номер месяца: '))

if user_month in winter:
    print(f'{user_month} это зима')
elif user_month in summer:
    print(f'{user_month} это лето')
elif user_month in autumn:
    print(f'{user_month} это осень')
elif user_month in spring:
    print(f'{user_month} это весна')

# 2-ое решение через словарь
seasons = {
    'Winter': [12, 1, 2],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11],
    'Spring': [3, 4, 5]
}
for key, value in seasons.items():
    if user_month in value:
        print(f"{user_month} month it's {key}")
        break
