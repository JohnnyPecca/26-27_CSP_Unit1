import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")

for t in range(18):
    painter.forward(20)
    painter.right(20)

wn = trtl.Screen()
wn.mainloop()