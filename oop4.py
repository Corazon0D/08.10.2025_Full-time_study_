# Основные понятия в ООП
# Полиморфизм (polymorphism)
# Свойство когда работать с разными типами данных
# Функция isinstance(объект, класс) -> True или False
# ДЗ добавить необходимые поля, вывод об объекте,
# Геттеры и Сеттеры
class Student:
    def __init__(self, u=''):
        self.university = u


class Employee:
    def __init__(self, c=''):
        self.company = c


class Person:
    def __init__(self, n=''):
        self.name = n


s = Student('Техноложка')
e = Employee('Авангард')
p = Person('Дима')

persons = [s, e, p]

for person in persons:
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
