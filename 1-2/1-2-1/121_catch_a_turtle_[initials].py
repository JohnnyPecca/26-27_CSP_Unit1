# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
#Entry = input(str("Start or Exit"))
#if Entry not in ("Start", "start"):

#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2

#-----initialize turtle-----
turtle = trtl.Turtle()
turtle.shape(spot_shape)
turtle.turtlesize(spot_size)
turtle.color(spot_color)
#-----game functions--------
def spot_clicked(X, Y):
    print("Spot was clicked!")




#-----events----------------

turtle.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()