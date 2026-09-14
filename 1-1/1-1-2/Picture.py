import turtle as trtl

# create turtle object
painter = trtl.Turtle()
Brush = float(input("YO CUH, HOW BIG U WANT THIS BRUSH TO BE? "))
Color = str(input("enter a color: "))

painter.pensize(Brush)
painter.color(Color) # added quotes around red

# move turtle without marking a line
painter.penup()
painter.goto(0, -325)
painter.pendown()

# Apply the fill color
painter.fillcolor(Color)
painter.begin_fill()
painter.circle(300, 360)  # Draw the circle
painter.end_fill()

# create screen object
wn = trtl.Screen()
wn.mainloop()