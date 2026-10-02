import turtle as trtl

color1 = "orange"
color2 = "purple"
wn = trtl.Screen()
width = 400
height = 300
painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "length"
while (answer == "length"):
    painter = trtl.Turtle()
    painter.speed(0)
    painter.color(color1)  # Set the starting color for the new turtle
    painter.goto(0, 0)
    angle = int(input("angle: "))
    seg = int(360 / angle)
    space = 1

    while painter.ycor() < height:
        # Change colors only every 100 spaces
        if space % 100 == 0:
            if painter.pencolor() == color2:
                painter.fillcolor(color1)
                painter.color(color1)
            else:
                painter.fillcolor(color2)
                painter.color(color2)

        painter.right(angle)
        painter.forward(2 * space + 10)
        painter.begin_fill()
        painter.circle(3)
        painter.end_fill()
        space = space + 1

    answer = input("again? (length/n): ")

wn.bye()