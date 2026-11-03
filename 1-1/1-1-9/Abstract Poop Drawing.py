
# Ask User for Input for Line or No Lines at top
stink = str(input("Does your poop stink? Answer Yes or No: "))

# Import Turtle for Drawing Purposes
import turtle as trtl

poop = trtl.Turtle()

# Define colors for future drawing
color1 = "brown"
color2 = "green"

painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
# Defining the
while stink not in ("yes", "no", "Yes", "No"):
    print("That was not a valid response.  Please check your spelling and try again.")
    stink = str(input("Does your poop stink? Answer Yes or No: "))

if stink in ("yes", "Yes"):
    print("temp")
elif stink in ("no", "No"):
    print("temp")





wn = trtl.Screen()
wn.mainloop()