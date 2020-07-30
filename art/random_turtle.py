from turtle import *
from random import random, randint, normalvariate
import sys

def round_to(x,g):
    return (round(x/g))*g 

colormode(255)
bgcolor('black')
pensize(20)
hideturtle()
speed(0)


from math import sin
def to_sin(x):
    return round(125.5 + 125.5*sin(x/100))

def spirals(ix):
    Screen().overridedirect(1)
    counter = 1
    direction = 0
    while 1:
        counter += 2
        pencolor( to_sin(counter),
                to_sin(counter*2) , to_sin(counter/2))
        direction = direction + normalvariate(0, 1)
        if direction > 3:
            direction = 0
        left(direction)
        forward(5)

def star(x):
    setpos(160,-80)
    Screen()
    counter = 1
    while 1:
        counter += 1
        pencolor( to_sin(counter),
                to_sin(counter*2) , to_sin(counter*3))
        left(x)
        forward(400)

def tw_point(ix):
    Screen()
    counter = 1
    while 1:
        w = window_width()
        h = window_height()
        x = randint( -(w//2) , w-(w//2) )
        y = randint( -(h//2) , h-(h//2) )
        d = distance(x, y)
        angle = towards(x, y)
        angle = round_to(angle,ix)
        setheading(angle)
        counter += 1
        pencolor( to_sin(counter) , to_sin(counter*2) , to_sin(counter/2))
        forward(d)

def hexa():
    Screen()
    while 1:
        pencolor((randint(1,255), randint(1,255), randint(1,255)))
        direction = random()*360
        direction = round_to(direction, 60)
        left(direction)
        forward(20)

if __name__ == '__main__':
    x = sys.argv[1]
    x = int(x)
    star(x)
