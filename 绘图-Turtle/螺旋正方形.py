import turtle


turtle.hideturtle()
turtle.pensize(2)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'green', 'blue']
turtle.speed(100)

# 打印螺旋线
for i in range(350):
    turtle.forward((2 * i))
    turtle.pencolor(colors[(i % 4)])
    turtle.left(91)

# 完成
print('已完成')
turtle.done()
