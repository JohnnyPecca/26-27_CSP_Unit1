import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor

num_floors = int(input("Enter Floors: "))

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    y = y + 5  # location of next floor
    rem = floor % 9
    if rem < 3:
        painter.color("gray")
    elif rem > 2 and rem < 6:
        painter.color("blue")
    else:
        painter.color("red")
    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()