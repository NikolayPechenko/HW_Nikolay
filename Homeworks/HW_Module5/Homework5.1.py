class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = int(floors)

    def go_to(self, new_floor):
        i = 1
        while new_floor >= i:
            if 0 < new_floor <= self.number_of_floors:
                print(i)
                i = i + 1
            else:
                print('Такого этажа не существует')
                break


h1 = House('ЖК Равнинный', 18)
h1.go_to(5)
h2 = House('Простоквашино', 2)
h2.go_to(10)
