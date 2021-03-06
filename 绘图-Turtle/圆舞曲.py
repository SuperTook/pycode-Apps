import turtle


turtle.speed(100)
turtle.hideturtle()
turtle.color('red')

turtle.tracer(5)
for x in range(80):
    turtle.forward(200)
    
    for y in range(237):
        turtle.left(1)
        turtle.forward(1)
        
    turtle.forward(100)
turtle.tracer(True)

turtle.done()
