class Car :
    #name = ""
    #color = ""

    def __init__(self , n, c):
        self.name = n
        self.color = c


    def start(self):
        print ("name: ", self.name)
        print ("color: ",self.color)
        print ("year: ",self.year)
        print ("Starting the engine ")

#creating a car an object


my_car1 = Car("Corolla", "White")
my_car1.year = 2017
my_car1.start()
my_car2 = Car("Premio", "Black")
my_car2.year = 2016
my_car2.start()
my_car3 = Car("Allion", "Blue")
my_car3.year = 2018
my_car3.start()
#my_car.name = input()
#my_car.color = input()
#print ("Name of car: ", my_car.name)
#print ("Color: ",my_car.color)
#print (dir(Car))
