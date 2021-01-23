#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.
class Devision:
    def __init__(self, divi):
        self.divi = divi

    def __str__(self):
        return str(self.divi)

    def __truediv__(self, other):
        if other.divi != 0:
            return self.divi / other.divi
        else:
            return 'Делить на 0 нельзя ! Попробуйте поменять значение для делителя.'


a = Devision(9)
b = Devision(3)
c = Devision(0)
print(a)
print(b)
print(a / b)
print(b / a)
print(a / c)
print(c / a)
