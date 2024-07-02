import abc

# class Horse:
#     def __init__(self):
#         self.x_distance = 0
#         self.sound = 'Frrr'
#         super().__init__()
#
#     def run(self, dx):
#         self.x_distance += dx
#
#
# class Eagle:
#     def __init__(self):
#         self.y_distance = 0
#         self.sound = 'I train, eat, sleep, and repeat'
#
#     def fly(self, dy):
#         self.y_distance += dy
#
#
# class Pegasus(Horse, Eagle):
#
#     pass
#
#     def move(self, dx, dy):
#         super().run(dx)
#         super().fly(dy)
#
#     def get_pos(self):
#         return self.x_distance, self.y_distance
#
#     def voice(self):
#         print(self.sound)
#
#
# p1 = Pegasus()
# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
# p1.voice()
# eagle = Eagle()
# eagle.fly(5)
# print(eagle.y_distance)
# horse = Horse()
#
#
# def land(eagle:Eagle):
#     eagle.fly(-eagle.y_distance)
#     return eagle.y_distance
#
#
# print(land(eagle))
# print(land(p1))

class Abstract_Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self, dy): pass

    @abc.abstractmethod
    def get_y_position(self): pass


class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle(Abstract_Bird):
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

    def get_y_position(self):
        return self.y_distance


class Pegasus(Abstract_Bird):
    def __init__(self):
        self.x_distance = 0
        self.y_distance = 0

    def run(self, dx):
        self.x_distance += dx

    def fly(self, dy):
        self.y_distance += dy

    def get_y_position(self):
        return self.y_distance

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance



p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
eagle = Eagle()
eagle.fly(5)
print(eagle.y_distance)
horse = Horse()


def land(bird:Abstract_Bird):
    bird.fly(-bird.get_y_position())


def print_bird_pos(bird:Abstract_Bird):
    print(bird.get_y_position())


land(eagle)
print_bird_pos(eagle)
print_bird_pos(p1)
