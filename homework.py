from random import choice


class Vehicle:

    __COLOR_VARIANTS = ['green', 'gray', 'serebro']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            self.__color = choice(self.__COLOR_VARIANTS)
            print(f'Невозможно создать машину с цветом {color}. Машина была создана в цвете {self.__color}')

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f"{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}" \
               f"\nВладелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя изменить цвет на '{new_color}'")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('serebro')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()