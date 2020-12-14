#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [5, 7, 5, 1, 1, 2, 3, 5]
sort = True
while sort:
    sort = False
    for i in range(len(my_list)-1):
        if my_list[i] < my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            sort = True
print('Current rating: ', my_list)
my_list.append(int(input('Enter new value for rating: ')))
print('New rating',my_list)
sort = True
while sort:
    sort = False
    for i in range(len(my_list)-1):
        if my_list[i] < my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            sort = True
print('New rating after sort', my_list)


