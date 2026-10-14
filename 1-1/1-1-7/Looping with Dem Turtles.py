
import turtle as trtl
my_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "gold", "purple", "#EFBFO4"]
for i in range(len(turtle_shapes)):
    t = trtl.Turtle(shape=turtle_shapes[i])
    t.color(turtle_colors[i])
    t.penup()
    my_turtles.append(t)
startx = 0
starty = 0
direction = 0
for t in my_turtles:
    t.goto(startx, starty)
    t.setheading(direction)
    t.pendown()
    t.forward(50)
    direction = direction + 60
wn = trtl.Screen()
wn.mainloop()