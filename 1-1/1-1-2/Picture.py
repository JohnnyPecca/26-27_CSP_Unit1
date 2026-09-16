import turtle as trtl

#Creating Turtle
painter = trtl.Turtle()

painter.penup()
painter.goto(-500, 500)
painter.pendown()

painter.pensize(1)

#Time of Day
tod = input("Please choose 'day' or 'night': ")

#Background
if tod == "day":
    painter.fillcolor("cyan")
    sky = "cyan"
    circle = "yellow"

else:
    painter.fillcolor("black")
    sky = "black"
    circle = "white"

#Draw background
painter.color(sky)
painter.fillcolor(sky)

painter.begin_fill()
painter.forward(1000)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.end_fill()

#Draw sun or moon
painter.penup()
painter.goto(350, 265)
painter.pendown()

painter.pensize(10)
painter.color(circle)
painter.fillcolor(circle)

painter.begin_fill()
painter.circle(60)
painter.end_fill()

#Draw grass
painter.penup()
painter.goto(-500, -200)
painter.pendown()

painter.pensize(1)
painter.color("green")
painter.fillcolor("green")

painter.begin_fill()
painter.forward(1000)
painter.right(90)
painter.forward(300)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.forward(300)
painter.right(90)
painter.end_fill()

painter.penup()

#create screen object
wn = trtl.Screen()
wn.mainloop()
