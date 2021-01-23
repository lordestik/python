#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date_str):
        self.date_str = str(date_str)

    def __str__(self):
        return f'{Date.figure(self.date_str)}'

    @classmethod
    def figure(cls, date_str):
        buf_list = date_str.split('-')
        return int(buf_list[0]), int(buf_list[1]), int(buf_list[2])

    @staticmethod
    def valid(day, month, year):
        if (1 <= day <= 31) and (1 <= month <= 12) and (0 <= year <= 2021):
            return f'Дата верна'
        else:
            return f'Что-то не так. Проверьте цифры в дате.'


mydate = Date('5-11-2012')
print(mydate)
print(Date.figure('21-11-1986'))
print(Date.valid(5, 7, 2017))
print(Date.valid(5, 13, 2017))
print(mydate.figure('11-09-2001'))
print(mydate.valid(11, 9, 2001))
