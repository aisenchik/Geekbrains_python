"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

from itertools import cycle
import time


class TrafficLight:
    def __init__(self, cycle_count=2):
        self.__color = ['red', 'yellow', 'green']
        self.__cycle_count = cycle_count * 3
        self.__times = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for i in cycle(self.__color):
            if self.__cycle_count:
                self.__cycle_count -= 1
            else:
                break
            print(i)
            time.sleep(self.__times[i])


traffic = TrafficLight()
traffic.running()