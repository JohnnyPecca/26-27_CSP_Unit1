import turtle as trtl

color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
wn.setup(width=600, height=600)

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle = 67

color_counter = 0

while space < 130:
    if (color_counter // 5) % 2 == 0:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)

    painter.right(angle)

    painter.forward(1.1 * 1 + 100)

    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()


wn.mainloop()

