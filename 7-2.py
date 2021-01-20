#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod
sqr = 0
class Cloth(ABC):

    def __init__(self, mount, param):
        self.mount = mount
        self.param = param

    @abstractmethod
    def summ(self, square):
        global sqr
        sqr = sqr + self.mount * square
        return self.mount * square



class Suit(Cloth):

    def __init__(self, mount, param ):
        self.param = param
        self.mount = mount
        print(f'Количество костюмов: {self.mount}. Рост костюма: {self.param}')

    @property
    def summ(self):
        return f'Общая площадь ткани для костюмов: {super().summ((2 * self.param + 0.3))}'


class Coat(Cloth):

    def __init__(self, mount, param):
        self.param = param
        self.mount = mount
        print(f'Количество пальто: {self.mount} Размер пальто: {self.param}')

    @property
    def summ(self):
        return f'Общая площадь ткани для пальто: {super().summ(round((self.param/6.5 + 0.5), 4))}'
        #return round((self.param/6.5 + 0.5), 4)


a = Suit(5, 5)
b = Coat(3, 3)
print(a.summ)
print(b.summ)
print(f'Общая площадь ткани, необходмая для производства всей продукции: {sqr}')
