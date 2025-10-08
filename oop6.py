# Основные понятия в ООП
# Специальные методы
class Time:

    def __init__(self, h=0, m=0):
        self.hour = h
        self.min = m

    def __info__(self):
        return f'{self.hour:02}:{self.min:02}'

    def __add__(self, other):
        h = self.hour + other.hour
        m = self.hour + other.min
        h += m // 60
        m = m % 60
        if h > 24:
            h -= 24
        return Time(h, m)

        return f'{self.hour:02}:{self.min:02}'

    def __str__(self):
        return f'{self.hour:02}:{self.min:02}'

    def __repr__(self):
        return f'{self.hour:02}:{self.min:02}'


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def info(self):
        return f'<P({self._x}, {self._y})>'

    # __str__ для отладки
    def __str__(self):
        return f'Point({self._x}, {self._y})'

    # __repr__ для отладки
    def __repr__(self):
        return f'Point({self._x}, {self._y})'

    # Сеттеры
    def set_x(self, new_x):
        self._x = new_x

    def set_y(self, new_y):
        self._y = new_y

    # Геттеры
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __sub__(self, other):  # Вычитание
        return Point(self._x - other._x, self._y - other._y)

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)


# t1 = Time(24, 30)
# t2 = Time(1, 45)
# print(t1 + t2)

p = Point(3, 5)
b = Point(2, 4)
print(p.get_y())
p.set_x(45)

print(p - b)
