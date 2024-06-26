class Building:
    total = 0

    def __init__(self):
        Building.total = Building.total + 1
        self.name = ''

    def __str__(self):  #  позволяет обращаться по имени без self
        return f'{self.name}'


houses = []
for i in range(40):
    house = Building()
    house.name = f'{i + 1} дом'
    houses.append(house)
    print(house)

print(Building.total, 'Домов')
