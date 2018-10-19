class Vehicle:
    """Base class for all Vehicle """

    def __init__(self, name, manufacture, color):
        self.name = name
        self.manufacture = manufacture
        self.color = color


class Car(Vehicle):
    """Car Class"""
    def __init__(self, name, manufacture, color, year):
        print("creating a car")
        super().__init__(name, manufacture,color)
        self.name = name
        self.year = 2017
        self.wheels = 4


if __name__ == "__main__":
    c = Car("Mustang 5.0 Gt Coupe", "Ford", "Red",2017)
    print(c.name, c.year, c.wheels)
    
    
