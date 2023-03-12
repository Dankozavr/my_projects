from turtle import *

speed(0)

diameter = 40
pop_diameter = 100
inflate_amount = 10

def draw_baloon():
    color("red")
    dot(diameter)
    return

def inflate_baloon():
    global diameter
    diameter += inflate_amount
    if diameter >= pop_diameter:
        hideturtle()
        clear()
        diameter = 40
        write("POP!")
    else:
        draw_baloon()
    return

draw_baloon()

onkey(inflate_baloon, "Up")
listen()
done()