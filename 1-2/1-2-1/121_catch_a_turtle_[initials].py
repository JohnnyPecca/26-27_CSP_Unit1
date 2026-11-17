
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
score = 0
font_setup = ("Arial", 20, "normal")
timer = 3
counter_interval = 1000
timer_up = False

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
for x in range(4):
    score_writers.right(90)
    score_writers.forward(100)
score_writers.penup()
score_writers.goto(315,315)
score_writers.pendown()
for x in range(4):
    score_writers.forward(100)
    score_writers.right(90)

score_writers.hideturtle()
counter = trtl.Turtle()

#-----game functions--------


def update_score():
    global score
    score += 1
    score_writers.clear()
    score_writers.write(score, font=font_setup)


def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_positon()
        update_score()
    else:
        spot.hideturtle()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)





def change_positon():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()
    spot.showturtle()



#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()