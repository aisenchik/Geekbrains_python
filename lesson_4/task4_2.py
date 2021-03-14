"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

orig_list = [123, 123, 43, 12, 21, 33, 1, 22, 4, 50, 85, 199, 100]
result_list = [orig_list[i] for i in range(len(orig_list)) if orig_list[i] > orig_list[i - 1] and i != 0]
print(result_list)
