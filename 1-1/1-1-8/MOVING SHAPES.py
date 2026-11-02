
import turtle as trtl


horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "classic", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "pink", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)


    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)


    tloc += 50


steps = 0
pixel_size = 20
distance = 3
while steps < 25:
    steps = steps + 1


    distance = 3
    distance = distance + 2
    if (distance > 10):
        distance = 3

    for ht in horiz_turtles:

        for vt in vert_turtles:


            ht.forward(distance)
            vt.forward(distance)


            if (abs(ht.xcor() - vt.xcor()) < pixel_size):
                if (abs(ht.ycor() - vt.ycor()) < pixel_size):
                    # remember color and shape of turtles
                    orig_ht_color = ht.fillcolor()
                    orig_ht_shape = ht.shape()
                    orig_vt_color = vt.fillcolor()
                    orig_vt_shape = vt.shape()


                    vt.fillcolor("gray")
                    vt.shape("circle")
                    vt.back(distance + 3)
                    ht.fillcolor("gray")
                    ht.shape("circle")
                    ht.back(distance + 3)


                    ht.shape(orig_ht_shape)
                    ht.fillcolor(orig_ht_color)
                    vt.shape(orig_vt_shape)
                    vt.fillcolor(orig_vt_color)

for ht in horiz_turtles:
    ht.fillcolor("gray")
for vt in vert_turtles:
    vt.fillcolor("gray")

wn = trtl.Screen()
wn.mainloop()