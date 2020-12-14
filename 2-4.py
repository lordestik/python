#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

str = input('Enter some string with several words with spaces: ')
list = str.split()
print(list)
for i in range(0,len(list)):
    print(f'{i+1}.{list[i][0:10]}')
