"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
new_file = []
with open('file_4.txt', encoding='utf-8') as file:
    for line in file:
        if line.split('—')[0].strip().lower() == 'one':
            new_file.append(line.lower().replace('one', 'один'))
        elif line.split('—')[0].strip().lower() == 'two':
            new_file.append(line.lower().replace('two', 'два'))
        elif line.split('—')[0].strip().lower() == 'three':
            new_file.append(line.lower().replace('three', 'три'))
        elif line.split('—')[0].strip().lower() == 'four':
            new_file.append(line.lower().replace('four', 'четыре'))

with open('file_4_upd.txt', 'w') as file:
    file.writelines(new_file)
