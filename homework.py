import math


class Figure:

    sides_count = 0

    def __init__(self, colors: list = None, sides: list = None,  filled: bool = False):
        self.filled = filled
        if self.__is_valid_sides(*sides):
            self.__sides = sides
        else:
            self.__sides = [1]*self.sides_count

        if self.__is_valid_color(*colors):
            self.__color = list(colors)
        else:
            self.__color = [0]*3

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if r in range(256) and g in range(256) and b in range(256):
            return True
        else:
            return False

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if side <= 0 or not isinstance(side, int):
                    return False
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, colors: list = None, sides: list = None):
        super().__init__(colors, [sides])
        self.__radius = len(self)/(2*math.pi)

    def get_square(self):
        return math.pi*(self.__radius**2)


class Triangle(Figure):

    sides_count = 3

    def __init__(self, colors: list = None, sides: list = None):
        super().__init__(colors, sides)
        self.__height = math.sqrt(self.get_sides()[0]**2 - (self.get_sides()[0]/2)**2)

    def get_square(self):
        half_per = len(self)/2
        return math.sqrt(half_per * (half_per-self.get_sides()[0]) * (half_per-self.get_sides()[1]) *
                         (half_per-self.get_sides()[2]))

class Cube(Figure):

    sides_count = 12

    def __init__(self, colors: list = None, side: int = 1):
        super().__init__(colors, [side]*self.sides_count)

    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())