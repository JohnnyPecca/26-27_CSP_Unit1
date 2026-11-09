
# Ask User if Poop Stinks
stink = str(input("Does your poop stink? Answer Yes or No: "))

# Import the Turtle
import turtle as trtl

poop = trtl.Turtle()
poop.speed(5)

# Define Colors
color1 = "brown"
color2 = "green"
color3 = "white"

# Check if the user inputted bullcrap
while stink not in ("yes", "no", "Yes", "No"):
    print("That was not a valid response. Try again.")
    stink = str(input("Does your poop stink? Answer Yes or No: "))

# Draw Bottom Circle
poop.penup()
poop.goto(0, -100)
poop.pendown()
poop.color(color1)
poop.begin_fill()
poop.circle(70)
poop.end_fill()

# Draw Middle Circle
poop.penup()
poop.goto(0, -40)
poop.pendown()
poop.begin_fill()
poop.circle(50)
poop.end_fill()

# Draw Top Circle
poop.penup()
poop.goto(0, 10)
poop.pendown()
poop.begin_fill()
poop.circle(30)
poop.end_fill()

# Draw Left Eye on the Poop
poop.penup()
poop.goto(-20, 15)
poop.pendown()
poop.color("black")
poop.begin_fill()
poop.circle(5)
poop.end_fill()

# Draw Right Eye on the Poop
poop.penup()
poop.goto(20, 15)
poop.pendown()
poop.begin_fill()
poop.circle(5)
poop.end_fill()

# Draw the Smile on the Poop
poop.penup()
poop.goto(-15, 0)
poop.setheading(-60)
poop.pendown()
poop.pensize(3)
poop.circle(18, 120)

# Draw the Green Stink Lines if the user said the Poop Stunk
if stink in ("yes", "Yes"):
    for z in range(1000000000000000000000000000000000):
        x = z % 2
        if (x == 0):
            poop.hideturtle()
            poop.color(color2)
            poop.pensize(5)

            poop.penup()
            poop.goto(-50, 100)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)

            poop.penup()
            poop.goto(0, 110)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)

            poop.penup()
            poop.goto(50, 100)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)
        if (x == 1):
            poop.hideturtle()
            poop.color(color3)
            poop.pensize(5)

            poop.penup()
            poop.goto(-50, 100)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)

            poop.penup()
            poop.goto(0, 110)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)

            poop.penup()
            poop.goto(50, 100)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)




    print("Your poop stinks!")

# Define what will happen if the user didn't say their poop stunk
elif stink in ("no", "No"):
    print("Your poop does not stink!")

# Hide the Turtle
poop.hideturtle()

# Make the Turtle Screen Appear
wn = trtl.Screen()
wn.mainloop()
