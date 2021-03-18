"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('file_2.txt') as file:
    print('Исходный файл:\n', '*' * 50)
    print(file.read(), '\n', '*' * 50)
    file.seek(0)
    for num, line in enumerate(file):
        print('Слов в {} строке - {}'.format(num, len(line.split())))
    file.seek(0)
    print('Количество строк в файле: ', len(file.readlines()))
