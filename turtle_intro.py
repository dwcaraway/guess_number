import turtle
import random

t = turtle.Pen()
t.speed(0)
t.shape("turtle")
t.color('green')
t.pensize(1)

COLORS = ["orange",
        "red",
        "blue",
        "green",
        "yellow",
        "violet"]

for x in range(100):
    #  t.pencolor(random.choice(COLORS))
    t.forward(2*x)
    t.left(90)

t.getscreen().exitonclick()
