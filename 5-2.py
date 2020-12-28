#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('text_2.txt', 'r')
str_count = 0
content = my_file.readline()
while content != '':
    str_count += 1
    string = content.split()
    print(f'Номер строки: {str_count} | Количество слов в строке: {len(string)}')
    content = my_file.readline()
print(f'Всего строк в файле: {str_count} ')
my_file.close()
