import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Configure the turtle drawer
pen = turtle.Turtle()
pen.color("red")
pen.speed(3)
pen.width(3)

# Draw a heart shape
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.setheading(60)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Write the text
pen.penup()
pen.goto(0, -50)  # Move inside the heart
pen.color("white")
pen.write("I LOVE YOU", align="center", font=("Arial", 24, "bold"))

# Keep window open
pen.hideturtle()
turtle.done()