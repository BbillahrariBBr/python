import turtle
turtle.color("blue")
height = 5
width = 5

turtle.speed(1)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.left(60)
    turtle.forward(20)
    turtle.right(60)

    #left/rigt(60) use for somodibahu triangle and 90 use for somokoni 
    
    width -=1
    #this line use for make triangle that means short width
turtle.exitonclick()
        
