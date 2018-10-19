class Vehicle:
    """Base class for all Vehicle """

    def __init__(self, name, manufacture, color):
        self.name = name
        self.manufacture = manufacture
        self.color = color


    def drive(self):
        print ("Driving ", self.manufacture, self.name)

    def turn(self, direction):
        print("Turning ",self.name, "to" , direction)

    def breake(self):
        print(self.name, " is stopping")

class Car(Vehicle):
    """Car Class"""

    def change_gear(self,gear_name):
        """Method for changing gear"""
        print(self.name, " is changing gear to ", gear_name)


if __name__ == "__main__":
    c = Car ("Mustang 5.0 Gt Coupe", "Ford", "Red")

    c.drive()
    c.breake()
    c.change_gear("p")
