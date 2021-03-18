"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
result = 0
with open('file_5.txt', 'w+', encoding='utf-8') as file:
    file.write('1 2 3 4 5 6 7 8')
    file.seek(0)
    for num in file.read().split(' '):
        result += int(num)
    print('Сумма чисел = ', result)
