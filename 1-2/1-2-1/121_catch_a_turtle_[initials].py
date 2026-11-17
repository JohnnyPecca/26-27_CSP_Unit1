
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
score = 0

#-----initialize spot-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.color(spot_color)
spot.penup()
score_writers = trtl.Turtle()
score_writers.penup()
score_writers.goto(-315,315)
score_writers.pendown()
score_writers.right(90)
score_writers.forward(100)
score_writers.right(90)
score_writers.forward(100)
score_writers.right(90)
score_writers.forward(100)
score_writers.right(90)
score_writers.forward(100)
score_writers.hideturtle()
#-----game functions--------


def update_score():
    global score
    score += 1
    score.writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)

def spot_clicked(x, y):
    change_positon()
    update_score()




def change_positon():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()
    spot.showturtle()



#-----events----------------
spot.onclick(update_score)
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()