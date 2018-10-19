import turtle
turtle.shape("turtle")
turtle.speed(1)

for side_length in range (50, 100, 10):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

turtle.exitonclick()
