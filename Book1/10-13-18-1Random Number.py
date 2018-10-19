import turtle
import random

#turtle.penup() #only for dot
#list of colrs

colors = ["red", "green", "blue", "yellow", "orange","black", "purple"]

for i in range(50):
    x = random.randint(-200,200)
    y = random.randint(-200,200)

    #set a random position
    turtle.setposition(x,y)

    #set a random color
    i = random.randint(0,len(colors)-1)
    turtle.dot(colors[i])

turtle.done()
