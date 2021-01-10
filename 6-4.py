# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:

    def __init__(self, speed, color, name, is_police):
        self.list = [speed, color, name, is_police]

    def go(self):
        print(f'Машина {self.list[2]} поехала')

    def stop(self):
        print(f'Машина {self.list[2]} остановилась')

    def turn(self, direct):
        print(f'Машина {self.list[2]} повернула {direct}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.list[2]} {self.list[0]}')

class TownCar(Car):

    def show_speed(self):
        if self.list[0] > 60:
            print(f'Осторожно !!! Вы привысили скорость. Ограничение скорости 60км/ч. Ваша скорость {self.list[0]}км/ч!')
        else:
            print(f'Текущая скорость автомобиля {self.list[2]} {self.list[0]}км/ч.')


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.list = [speed, color, name, is_police]
        if self.list[3] == True:
            self.list[2] = 'Полицейский ' + self.list[2]


class WorkCar(Car):

    def show_speed(self):
        if self.list[0] > 40:
            print(
                f'Осторожно !!! Вы привысили скорость. Ограничение скорости 40км/ч. Ваша скорость {self.list[0]}км/ч!')
        else:
            print(f'Текущая скорость автомобиля {self.list[2]} {self.list[0]}км/ч.')


a = TownCar(62, 'red', 'mazda', False)
a.go()
a.stop()
a.turn('налево')
a.show_speed()

b = WorkCar(35, 'red', 'Opel', False)
b.go()
b.stop()
b.turn('направо')
b.show_speed()

c = SportCar(90, 'white', 'Ferrari', False)
c.go()
c.stop()
c.turn('направо')
c.show_speed()

d = PoliceCar(90, 'white', 'Lada', True)
d.go()
d.stop()
d.turn('направо')
d.show_speed()
