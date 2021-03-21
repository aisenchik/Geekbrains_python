"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула')

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость равна', self.speed)
        if self.speed > 60:
            print('ВНИМАНИЕ!!! Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость равна', self.speed)
        if self.speed > 40:
            print('ВНИМАНИЕ!!! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, police_number, speed, color='White', name='Police Ford', is_police=True):
        super().__init__(speed, color, name, is_police)
        self.police_number = police_number


police = PoliceCar(speed=50, police_number=123)
police.go()
police.turn()
police.show_speed()
print(police.color)

work = WorkCar(speed=50, color='black', name='Toyota')
work.go()
work.turn()
work.show_speed()
print(work.color)

town = WorkCar(speed=100, color='blue', name='BMW')
town.go()
town.turn()
town.show_speed()
print(town.color)