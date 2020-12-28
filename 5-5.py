#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open('text-5.txt', 'w+')
summa = 0
mylist = []
for i in range(0,100,5):
    my_file.write(str(i) + ' ')
my_file.seek(0)
li = my_file.readlines()[0].split()
for i in li:
    mylist.append(int(i))
    summa = summa + int(i)
print(f'Строка с числами из файла: {mylist}')
print(f'Сумма чисел в числовой строке: {summa}')
my_file.close()
