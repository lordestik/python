# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое
# слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# Функция. Так же реализована проверка слова.
def int_func(word):
    for i in range(0, len(word)):
        if (ord(word[i]) < 97) or (ord(word[i])) > 122:
            print('slovo ne podhodit')
            return
    word = chr(ord(word[0])-32) + word[1:len(word)]
    return word

str = input('введите строку: ')
list = str.split()
buf_list = list.copy()  # пришлось создать буферный список, т.к. в цикле for, в котором прохожусь по списку,
# удаляю элементы из этого же списка.
str = ''    # обнуляю исходную строку, т.к. в задании нужно сделать вывод именно исходной строки(я так понял использовать
# туже переменную)
for value in buf_list:  # прохожусь по словам в списке
    for i in range(0, len(value)):  # прохожусь по символам в слове
        if (ord(value[i]) < 97) or (ord(value[i])) > 122: # проверяю символы в слове на принадлежность к ('a':'z')
            #print(value)
            list.remove(value)  # удаяю элемент из списка (из-за этого действия пришлось сделать буферный список)
            break
#print(list)
#print(buf_list)
for value in list:
    str = str + ' ' + int_func(value)   # формирую финальное значение строки в изначальной переменной этой строки
print(str)
