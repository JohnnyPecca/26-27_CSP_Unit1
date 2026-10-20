
import turtle as trtl
my_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "classic", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "gold", "gold", "gold"]
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.color(turtle_colors.pop())
    my_turtles.append(t)
startx = 0
starty = 0
direction = 90
spiral = 50
for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.setheading(direction)
    t.pendown()
    t.right(45)
    t.forward(spiral)
    spiral += 10
    direction = t.heading()


    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()