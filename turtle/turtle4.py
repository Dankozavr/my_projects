'''
@author: Daniil Ivanov
@note: Turtle run for the ocean
'''
from turtle import *

def draw_map():
    bgcolor("orange")
    color("blue")
    penup()
    goto(width / 2 - 400, height / 2)
    begin_fill()
    pendown()
    goto(width / 2, height / 2)
    goto(width / 2, - height / 2)
    goto(width / 2 - 400, - height / 2)
    goto(width / 2 - 400, height / 2)
    end_fill()

def reset():
    penup()
    goto(-200, 0)
    shape("turtle")
    color("green")

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(-90)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() >= width / 2 - 400:
        hideturtle()
        goto(0, 0)
        clear()
        color("white")
        write("YOU WIN")

if __name__ == "__main__":
    speed(0)

    move_distance = 20
    width = window_width()
    height = window_height()

    draw_map()
    reset()
    
    onkey(move_up, "Up")
    onkey(move_left, "Left")
    onkey(move_right, "Right")
    onkey(move_down, "Down")
    listen()
    done()

