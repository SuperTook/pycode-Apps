import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed(100)
turtle.color('red', 'yellow')

# 走36次
for i in range(36):
    turtle.forward(400)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

print('已完成')
turtle.done()
