# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand



#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial",20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(200,200)

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-200, 200)

#-----game functions--------
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()
    spot.showturtle()

def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_position()
        update_score()
    else:
        spot.hideturtle()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
      counter.write("Time's Up", font=font_setup)
      timer_up = True
      manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def manage_leaderboard():
    global score
    global spot
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)


#-----events---------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()