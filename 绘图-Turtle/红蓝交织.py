import turtle
n = 500
turtle.hideturtle()
turtle.penup()
turtle.goto(-250, 100)
turtle.pendown()

for i in range(1,850):
 
    if i < 500:
        n -= 1
        turtle.speed(100)
        turtle.pencolor("blue")
        turtle.fd(n)
        turtle.right(140)
    else:
        n += 1
        turtle.speed(100)
        turtle.pencolor('red')
        turtle.fd(n)
        turtle.right(110)

print('已完成')
turtle.done()
