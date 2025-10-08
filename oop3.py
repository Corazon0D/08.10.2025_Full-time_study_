# Основные понятия в ООП
# Полиморфизм (polymorphism)
# Свойство когда работать с разными типами данных

# print(3 + 5)
# print('3' + '5')
# print([3] + [5])
# print(2.5 + 3.4)
from math import pi


# Полиморфна функция

def print_shape_info(shape: object) -> None:
    """
    Распечатывает информацию о площади и периметре объекта
    :param shape: объетк: квадрат, круг,...
    :param object: None
    :return:
    """
    figure = None
    figure_class = type(shape)
    if shape.__class__.__name__ == 'Square':
       figure = 'Квадрата'
    if shape.__class__.__name__ == 'Circle':
       figure = 'Круга'
    if shape.__class__.__name__ == 'Rectangle':
       figure = 'Прямоугольника'
    if shape.__class__.__name__ == 'Triangle':
       figure = 'Треугольника'
    print(f'Площадь {figure}: {shape.square()}\nПериметр {figure}: {shape.perimeter()}')


class Circle:
    def __init__(self, r=1):
        self._radius = r

    def perimeter(self):
        return 2 * pi * self._radius

    def square(self):
        return pi * (self._radius ** 2)


class Square:
    def __init__(self, s=1):
        self._side = s

    def perimeter(self):
        return 4 * self._side

    def square(self):
        return self._side ** 2


class Rectangle:  # Прямоугольник
    def __init__(self, s1=1, s2=2):
        self._side1 = s1
        self._side2 = s2

    def perimeter(self):
        return 2 * (self._side1 + self._side2)

    def square(self):
        return self._side1 * self._side2


class Triangle:  # Треугольник
    def __init__(self, s1=5, s2=7, s3=9):
        self._side1 = s1
        self._side2 = s2
        self._side3 = s3

    def perimeter(self):
        return self._side1 + self._side2 + self._side3

    def square(self):
        return self._side1 ** 2


s = Square(5)  # Квадрат со стороной 5
c = Circle(5)  # Окружность с радиусом 5
r = Rectangle()
t = Triangle()
print_shape_info(s)
print_shape_info(c)
print_shape_info(r)
print_shape_info(t)
