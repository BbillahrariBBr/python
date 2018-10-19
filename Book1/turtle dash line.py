import turtle
turtle.shape("turtle")
turtle.speed(1)

for a in range (2):
    for i in range(3):
        for  j in range (5):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(3)
            turtle.pendown()
        turtle.left(120)
turtle.exitonclick()
