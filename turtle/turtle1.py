from turtle import *
speed(0)
hideturtle()

def Draw(c, r, m):
    begin_fill()
    color(c)
    circle(r)
    end_fill()
    penup()
    forward(m)
    pendown

bgcolor("black")
Draw("orange", 60, 100)
Draw("grey", 20, 80)
Draw("red", 40, 90)
Draw("green", 30, 0)
done()