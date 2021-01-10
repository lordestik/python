# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.
class Stationery:
    title = 'Канцелярскими принадлежностями'

    def draw(self):
        print(f'Запуск отрисовки {Stationery.title}.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title}. Это Ручка')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title}. Это Карандаш')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title}. Это Маркер')


a = Stationery()
b = Pen()
c = Pencil()
d = Handle()

a.draw()
b.draw()
c.draw()
d.draw()
