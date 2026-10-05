import turtle
import random

# Set up the screen and turtle for the NYC skyline
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#0B1D3A")
screen.title("NYC Skyline - Python Turtle")

# TURN OFF ANIMATION UPDATES FOR INSTANT RENDERING
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Draw background stars
for _ in range(40):
    draw_rectangle(random.randint(-380, 380), random.randint(50, 280), random.randint(1, 3), random.randint(1, 3), "white")

# Buildings data
buildings = [
    (-350, 50, 250, "#1F2937"),
    (-295, 70, 320, "#374151"),
    (-220, 45, 180, "#111827"),
    (-170, 90, 380, "#1F2937"),
    (-75, 60, 220, "#374151"),
    (-10, 80, 300, "#1F2937"),
    (75, 50, 160, "#111827"),
    (130, 85, 350, "#374151"),
    (220, 60, 270, "#1F2937"),
    (285, 55, 200, "#111827")
]

# Draw buildings with lit windows
for b_x, b_width, b_height, b_color in buildings:
    draw_rectangle(b_x, -250, b_width, b_height, b_color)
    for w_x in range(b_x + 10, b_x + b_width - 15, 15):
        for w_y in range(-230, -250 + b_height - 20, 25):
            if random.random() > 0.3:
                draw_rectangle(w_x, w_y, 8, 12, "#FACC15")

# Draw foreground/ground
draw_rectangle(-400, -260, 800, 15, "#030712")

# FORCE THE SCREEN TO UPDATE AT THE VERY END
screen.update()

turtle.done()