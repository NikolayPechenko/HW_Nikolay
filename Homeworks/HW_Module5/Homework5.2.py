class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors
        print('Новое число этажей', self.number_of_floors)


k530 = House()
k530.set_new_number_of_floors(14)
