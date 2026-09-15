import turtle as trtl

# create turtle object
painter = trtl.Turtle()

Color = str(input("Enter a color lil bro"))

painter.pensize(10)
painter.color(Color)

# move turtle without marking a line
painter.penup()
painter.goto(350, 265)
painter.pendown()

# Draw the Sun
painter.fillcolor(Color)
painter.begin_fill()
painter.circle(60, 360)  # Draw the circle
painter.end_fill()

#Assign the Grass
painter.penup()
painter.goto(-500, -200)
painter.pendown()
painter.color("green")

#color
painter.fillcolor("green")
painter.begin_fill()
painter.forward(1000)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.end_fill()


#Move turtle
painter.penup()




# create screen object
wn = trtl.Screen()
wn.mainloop()
