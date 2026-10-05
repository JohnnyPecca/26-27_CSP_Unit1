# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.circle(20)

# Make Spider Legs
leg = 14
length = 70
angle = 360 / leg
x.pensize(5)
n = 0
while (n < leg):
  x.goto(0,0)
  x.setheading(angle*n)
  x.forward(length)
  n = n + 1
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()