# Основные понятия в ООП
# Инкапсуляция (encapsulation)

# class Fruit:
#     counter = 0  # Статичный член класса
#
#     def __init__(self, n='Фрукт', w=0, c='Белый'):
#         self.name = n
#         self.washed = w
#         self.color = c
#         Fruit.counter += 1 # Увеличиваем счётчик экземпляров
#
#     def wash(self):
#         print(f'Фрукт {self.name} помыт')
#
#     def about_me(self):
#         print(f'Я фрукт {self.name}, который весит {self.washed}')
#         print(f'А цвет у меня {self.color}')
#
#     @staticmethod
#     def get_count():
#         return Fruit.counter
#
#
# f1 = Fruit('Груша', 250, 'Зелёный')
# f1.about_me()
# f1.wash()
# f2 = Fruit('Яблоко', 210, 'Красный')
# f2.about_me()
# f2.wash()
# f3 = Fruit('Лимон', 310, 'Жёлтый')
# f3.about_me()
# f3.wash()
# print('Итого фруктов:', Fruit.get_count())


# class Person:
#     _counter = 0  # Статичный счётчик класса (счётчик персон, защищённый)
#
#     def __init__(self, n='Noname', a=0, nat='Страна'):
#         self._name = n
#         self._age = a
#         self._nationality = nat
#         Person._counter += 1  # Увеличиваем счётчик экземпляров
#
#     def wash(self):
#         print(f'Фрукт {self._name} помыт')
#
#     def about_me(self):
#         print(f'Я  {self._name}, мой возраст {self._age}')
#         print(f'Я из {self._nationality}')
#
# # Setter (Сеттро)
#     def set_age(self, new_age):
#         if new_age > 0 and new_age <= 125:
#             self._age = new_age
#         else:
#             print('Недопустимое значение для возраста')
#
#     def set_name(self, new_name): # Делаем новое имя
#         if len(new_name) > 3:
#             self._name = new_name
#
#     def set_nationality(self, new_nation):
#         if len(new_nation) > 1:
#             self._nationality = new_nation
#
#
# # Getter (Геттеры) то что возвращает
#     def get_age(self):
#         return self._age
#
#
#     def get_name(self):
#         return self._name
#
#     @staticmethod
#     def get_count():
#         return Person._counter
#
# p1 = Person('John', 27, 'USA')
# p1.set_age(-25)
# p1.about_me()
# print('Итак, его зовут -', p1.get_name())
# print('Всего персон:', Person.get_count()) # We are all a


class Car:
    _counter = 0  # Статичный счётчик класса (счётчик персон, защищённый)

    def __init__(self, b='Noname', m='Model'):
        self._brand = b
        self._madel = m
        self._engine_on = False
        Car._counter += 1  # Увеличиваем счётчик экземпляров

    # Сокрытие информации о внутреннем устройстве за внешним интерфейсом
    # И есть инкапсуляция
    def engine_start(self):
        self._engine_on = True



    def drive(self, place):
        if self._engine_on:
            print('Пункт назначения:', place)
        else:
            print('Двигатель не заведён, никуда не едем!')

    # Геттеры
    def get_brand(self):
        return self._brand

    def get_madel(self):
        return self._madel

    # Сеттеры
    def set_brand(self, new_brand):
        self._brand = new_brand

    def set_model(self, new_madel):
        self._brand = new_madel

    def about_car(self):
        print('Автомобиль:')
        print('\t Марка:', self._brand)
        print('\t Модель:', self._madel)

    @staticmethod
    def get_count():
        return Car._counter



