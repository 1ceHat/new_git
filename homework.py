from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_enemy = 100
        count_day = 0
        while count_enemy > 0:
            count_enemy -= self.power
            time.sleep(1)
            count_day += 1
            print(f'{self.name} сражается {count_day}, осталось {count_enemy} воинов')

        print(f'{self.name} одержал победу спустя {count_day} дней (дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
