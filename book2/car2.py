class Vehicle:
    """Base class for all Vehicle """

    def __init__(self, name, manufacture, color):
        self.name = name
        self.manufacture = manufacture
        self.color = color

    def turn(self, direction):
        print("Turning ",self.name, "to" , direction)

class Car(Vehicle):
    """Car Class"""
    def __init__(self, name, manufacture, color, year, wheels):
        self.name = name
        self.manufacture = manufacture
        self.color = color
        self.year = 2017
        self.wheels = 4
        
    def change_gear(self,gear_name):
        """Method for changing gear"""
        print(self.name, " is changing gear to ", gear_name)

     #turn method is overriding   
    def turn(self, direction):
        print("Turning ",self.name, "is turing" , direction)


if __name__ == "__main__":
    c = Car ("Mustang 5.0 Gt Coupe", "Ford", "Red",2018, 4)
    v = Vehicle("Softail Delux", "Harley-Davidson", "blue")

    c.turn("right")
    v.turn("left")
    
