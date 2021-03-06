import turtle

turtle.hideturtle()
turtle.tracer(6)
pen = turtle.Turtle()
pen.speed(100)

for i in range(271):
    pen.forward(200)
    pen.right(30.1)
    pen.forward(20)
    pen.left(60.1)
    pen.forward(100)

    pen.penup()
    pen.setposition(0, 0)
    pen.fd(13)
    pen.pendown()

    pen.right(2.1)
turtle.done()