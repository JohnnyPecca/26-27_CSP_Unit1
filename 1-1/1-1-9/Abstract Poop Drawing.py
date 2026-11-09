
# Ask User if Poop Stinks
stink = str(input("Does your poop stink? Answer Yes or No: "))

# Import the Turtle
import turtle as trtl

poop = trtl.Turtle()
poop.speed(0)

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

poopX = -20
for x in range(2):
    poop.penup()
    poop.goto(poopX, 15)
    poop.pendown()
    poop.color("black")
    poop.begin_fill()
    poop.circle(5)
    poop.end_fill()
    poopX += 40


# Draw the Smile on the Poop
poop.penup()
poop.goto(-15, 0)
poop.setheading(-60)
poop.pendown()
poop.pensize(3)
poop.circle(18, 120)

poop.speed(5)
currentColor = ""
# Draw the Green Stink Lines if the user said the Poop Stunk
if stink in ("yes", "Yes"):
    for z in range(1000000000000000000000000000000000):
        x = z % 2
        if (x == 0):
            currentColor = color2
        if (x == 1):
            currentColor = color3

        poop.hideturtle()
        poop.color(currentColor)
        poop.pensize(5)

        xStart = -50
        for y in range(3):
            poop.penup()
            poop.goto(xStart, 100)
            poop.setheading(90)
            poop.pendown()
            poop.forward(40)
            xStart += 50





    print("Your poop stinks!")

# Define what will happen if the user didn't say their poop stunk
elif stink in ("no", "No"):
    print("Your poop does not stink!")

# Hide the Turtle
poop.hideturtle()

# Make the Turtle Screen Appear
wn = trtl.Screen()
wn.mainloop()
