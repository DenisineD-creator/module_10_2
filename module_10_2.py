import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} дней(дня)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней!')




first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы окончены!')