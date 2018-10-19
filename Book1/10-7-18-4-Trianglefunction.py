import turtle
turtle.speed(5)

def draw_triangle(side_length):
    turtle.forward(side_length)
    turtle.left(120)

counter = 0
while counter<180:
    draw_triangle(100)
    turtle.right(7)
    counter += 1

turtle.exitonclick()
