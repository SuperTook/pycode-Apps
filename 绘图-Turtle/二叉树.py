from turtle import *

# 设置色彩模式是RGB:
colormode(255)

left(90)

lv = 16
l = 120
s = 45

pensize(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
back(l + l / 2)
pendown()
forward(l)


def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = pensize()

    # narrow the pen width
    pensize(w * 3 / 4)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    left(s)
    forward(l)

    if level < lv:
        draw_tree(l, level + 1)
    back(l)
    right(2 * s)
    forward(l)

    if level < lv:
        draw_tree(l, level + 1)
    back(l)
    left(s)

    # restore the previous pen width
    pensize(w)


speed("fastest")
hideturtle()
tracer(200)
draw_tree(l, 4)
tracer(True)
done()