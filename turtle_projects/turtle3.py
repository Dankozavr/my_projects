'''
@author: Daniil Ivanov
@note: Drawing starry space
'''
from random import *
from turtle import *

def generate_numbers():
    position_x = randrange(round(-width / 2), round(width / 2))
    position_y = randrange(round(-height / 2), round(height / 2))
    size = randrange(1, 10)
    return position_x, position_y, size

def draw_star(x, y, size):
    penup()
    goto(x, y)
    pendown()
    dot(size, "white")

if __name__ == "__main__":
    speed(0)
    bgcolor("black")
    
    number_of_stars = 100
    width = window_width()
    height = window_height()

    for i in range(number_of_stars):
        x, y, size = generate_numbers()
        draw_star(x, y, size)
