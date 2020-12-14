#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month_number = int(input('Enter the integer number for month: '))
dict = {'Winter': (31, 1, 2), 'Spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}
if  (0 < month_number <= 12):
    for i in range(0,3):
        if month_number == (dict['Winter'][i]):
            print('This is Winter')
        elif month_number == (dict['Spring'][i]):
            print('This is Spring')
        elif month_number == (dict['Summer'][i]):
            print('This is Summer')
        elif month_number == (dict['Autumn'][i]):
            print('This is Autumn')
else:
    print('The number must be integer and more then 0 and less then 13 !!!')

