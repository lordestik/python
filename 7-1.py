# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        local_list = []
        for i in self.lists:
            for j in range(0, len(i)):
                if j == len(i) - 1:
                    local_list.append(str(i[j]) + '\n')
                else:
                    local_list.append(str(i[j]) + '\t')
        return ''.join(local_list)

    def __add__(self, other):
        sum_matrix = []
        elem_matrix = []
        try:
            for m in range(0, len(self.lists)):
                for n in range(0, len(self.lists[m])):
                    elem_matrix.append(int(self.lists[m][n]) + int(other.lists[m][n]))
                sum_matrix.append(elem_matrix)
                elem_matrix = []
            return Matrix(sum_matrix)
        except IndexError:
            return f'Error'


mylist = [[1, 2, 3], [4, 5, 6], [7, 8], [9, 10, 11]]
mylist2 = [[1, 2, 3], [4, 5, 6], [7, 8], [9, 10, 11]]
a = Matrix(mylist)
b = Matrix(mylist2)
print(a + b)