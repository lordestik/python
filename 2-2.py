#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
list_len = int(input('Enter list length: '))
list = []
for i in range(0,list_len):
    list.append(input('Enter element of list: '))
print(list)
for i in range(0,list_len,2):
    if i >= list_len-1:
        break
    list[i], list[i+1] = list[i+1], list[i]
print(list)
