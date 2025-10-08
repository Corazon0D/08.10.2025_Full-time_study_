# Реализация класса Car
from oop2 import Car

def main():
    car1 = Car('Lada', 'Kalina')
    car1.about_car()
    car1.engine_start()  # сначала завели двигатель
    car1.drive('дача')

    print('Машина в гараже:', Car.get_count())

if __name__ == '__main__':
    main()
