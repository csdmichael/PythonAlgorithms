class Vehicle:
    name = ""
    kind = "Car"
    color = ""
    value = 100.00

    def __init__(self, name, color, kind, value):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value

    def description(self) -> str:
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle("Car 1", "red", "convertible", 60000)
car2 = Vehicle("Car 2", "blue", "Van", 100000)

d1 = car1.description()
print(d1)

d2 = car2.description()
print(d2)