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


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 Ex", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustang 50.GT", "Ford", "Red")


    v1.drive()
    v2.drive()
    v3.drive()


    v1.turn("left")
    v2.turn("Right")

    v1.breake()
    v2.breake()
    v3.breake()
    
