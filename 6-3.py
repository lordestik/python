# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:

    def __init__(self, name, surname, position, income):
        self.my_list = [name, surname, position]
        self._inc = income


class Position(Worker):

    def get_full_name(self):
        print(self.my_list[0] + ' ' + self.my_list[1])

    def get_total_income(self):
        print(self._inc.get('wage') + self._inc.get('bonus'))


a = Position('Leonid', 'Bukreev', 'IT', {"wage": 1500, "bonus": 500})
a.get_full_name()
a.get_total_income()

b = Position('Vlada', 'Gorovenko', 'HR', {'wage': 1700, 'bonus': 500})
b.get_full_name()
b.get_total_income()
