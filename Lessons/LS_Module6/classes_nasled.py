class Human:
    def __init__(self, name, group):
        super().__init__(group)
        self.name = name
        self.about()

    def info(self):
        print(f'Привет, меня зовут {self.name}')
        a = 2
        return a


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')



class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()

    def info(self):
        print('privet')


# human = Human('Kio', 4)
# print(human.name)
student = Student('Mimo', 'FU', 'Питон')
# print(student.name, student.place)
# student.about()
print(student.info())