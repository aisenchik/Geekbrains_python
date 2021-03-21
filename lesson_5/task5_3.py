"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

average_salary = []
with open('file_3.txt') as file:
    for line in file:
        emp, salary = line.split()
        average_salary.append(float(salary))
        if float(salary) < 20000:
            print(f'{emp} с доходом {salary}')
    print('Средний доход сотрудников: ', sum(average_salary) / len(average_salary))

