import turtle as trtl

wn = trtl.Screen()
wn.tracer(0)

# Draw the spider
x = trtl.Turtle()
x.speed(0)
x.pensize(40)
x.circle(20)
length = 70
x.pensize(5)
leg_angles = [20, 40, -20, -40, 140, 160, 200, 220]
n = 0
while n < len(leg_angles):
  x.goto(0, 20)
  x.setheading(leg_angles[n])
  x.forward(length)
  n = n + 1
x.hideturtle()

# Draw the other creature/bug
p = trtl.Turtle()
p.speed(0)
p.hideturtle()
p.color("#8B4513")  # Saddle brown color
p.penup()
p.goto(-150, -40)
p.pendown()
p.begin_fill()
p.circle(40)
p.end_fill()
p.penup()
p.goto(-150, 10)
p.pendown()
p.begin_fill()
p.circle(30)
p.end_fill()
p.penup()
p.goto(-150, 50)
p.pendown()
p.begin_fill()
p.circle(18)
p.end_fill()
p.color("black")
p.penup()
p.goto(-160, 45)
p.pendown()
p.begin_fill()
p.circle(4)
p.end_fill()
p.penup()
p.goto(-140, 45)
p.pendown()
p.begin_fill()
p.circle(4)
p.end_fill()
p.penup()
p.goto(-155, 32)
p.setheading(-60)
p.pendown()
p.pensize(2)
p.circle(7, 120)

# Draw speech bubble above the spider
s = trtl.Turtle()
s.speed(0)
s.hideturtle()
s.penup()
s.color("black", "white")

s.goto(-115, 90)
s.pendown()
s.begin_fill()
for _ in range(2):
  s.forward(230)
  s.left(90)
  s.forward(40)
  s.left(90)
s.end_fill()

s.penup()
s.goto(-10, 90)
s.pendown()
s.begin_fill()
s.goto(0, 50)
s.goto(10, 90)
s.goto(-10, 90)
s.end_fill()

# Write the text
s.penup()
s.color("black")
s.goto(0, 102)
s.write("I just took a giant dump", align="center", font=("Arial", 9, "bold"))

wn.update()
wn.mainloop()