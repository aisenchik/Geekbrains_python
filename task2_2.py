'''
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

user_list = []
num_elements = int(input('Введите количество элементов: '))
for inp in range(1, num_elements + 1):
    element = input(f'Введите {inp}-й элемент списка: ')
    user_list.append(element)

work_list = user_list.copy()
i = 0
for num in range(len(user_list)):
    print(i, num)
    work_list[num + i], work_list[num + 1 + i] = work_list[num + 1 + i], work_list[num + i]
    if len(user_list) % 2 == 0:
        if num + i + 2 == len(work_list):
            break
    elif num + i + 3 == len(work_list):
        break
    i += 1
print('Введеный список: ', user_list)
print('Измененный список: ', work_list)
