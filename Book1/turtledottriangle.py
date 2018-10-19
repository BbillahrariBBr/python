import turtle
turtle.color("purple")

height = 5
width = 5

turtle.speed(1)
turtle.penup()

for x in range(height):
    for y in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(60)
    turtle.forward(20)
    turtle.left(60)
    width -= 1

turtle.exitonclick
        
