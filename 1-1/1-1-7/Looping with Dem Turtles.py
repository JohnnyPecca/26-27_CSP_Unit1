
import turtle as trtl
my_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "arrow"]
turtle_colors = ["red", "blue", "green", "gold", "purple", "yellow"]
for i in range(len(turtle_shapes)):
    t = trtl.Turtle(shape=turtle_shapes[i])
    t.color(turtle_colors[i])
    t.penup()
    my_turtles.append(t)
startingx = 0
startingy = 0
direction = 0
for t in my_turtles:
    t.goto(startingx, startingy)
    t.setheading(direction)
    t.pendown()
    t.forward(50)
    direction = direction + 60
wn = trtl.Screen()
wn.mainloop()