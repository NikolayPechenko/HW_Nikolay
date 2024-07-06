import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__color = color
        self.filled = filled
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r < 256 and 0 <= g < 256 and 0 <= b < 256:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        a = 1
        if len(sides) == self.sides_count:
            for side in sides:
                if isinstance(side, int) and side > 0:
                    a *= 1
                else:
                    a *= 0
        else:
            a = 0
        return bool(a)

    def set_sides(self, *side):
        if self.sides_count == 12:
            if len(side) == 1 and side[0] > 0:
                self.__sides = []
                for i in range(12):
                    self.__sides.append(*side)
        else:
            if self.__is_valid_sides(*side):
                self.__sides = list(side)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        for i in self.__sides:
            p += i
        return p


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = self.get_sides()[0] / 2 / math.pi

    def get_square(self):
        return self.__radius * self.__radius * math.pi

    def www(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__height = self.get_square() / (len(self)/2) * 2

    def get_square(self):
        p = len(self)/2
        a = (self._Figure__sides[0])
        b = (self._Figure__sides[1])
        c = (self._Figure__sides[2])
        s = (p * (p-a)*(p-b)*(p-c)) ** 0.5
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == 1:
            self._Figure__sides = []
            for i in range(12):
                self._Figure__sides.append(*sides)
        else:
            for i in range(12):
                self._Figure__sides = [1]

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
