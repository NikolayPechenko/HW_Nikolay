class Building:
    def __init__(self, floors, types):
        self.numberOfFloors = int(floors)
        self.buildingType = str(types)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


H1 = Building(24, "MDK")
H2 = Building(25, "MJK")
print(H1 == H2)
