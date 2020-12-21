# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

buf = input('Введите список целых чисел (другие элементы будут игнорироваться): ').split()
list = []
for item in buf:
    try:
        list.append(int(item))
    except ValueError:
        None
print(f'Список без лишних элементов: {list}')
new_list = [i for i in list if list.count(i) == 1]

print(f'Итоговый массив чисел: {new_list}')

