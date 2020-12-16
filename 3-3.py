#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.
"""решил сделать универсальную функцию для нахождение наибольшей суммы для любого количества аргументов,
если добавить функции больше аргументов.
"""

def my_func(*args):
    list = []
    for i in args:
        list.append(i)
    #print(list)
    sort = True
    while sort:
        sort = False
        for i in range(1, len(list)):
            if list[i-1] < list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                sort = True
    #print(list)
    return list[0] + list[1]

print(my_func(9, 11, -17, 23, 7))

