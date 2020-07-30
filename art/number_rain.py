import colors as c
from random import random, randint, shuffle, choice
from time import sleep
from colors import show_cursor, hide_cursor
import numpy as np

def bar():
    return choice('01234567890')

def adjust_clr(triple, target):
    new = []
    for a in range(3):
        value = -1
        while value < 0 or value > 255:
            value = round(triple[a]+(random()*(target[a]-triple[a])))
        new.append(value)
    return new

def draw(size):
    color = [100,123,200]
    string = ''
    for i in range(size):
        color = adjust_clr(color)
        string = string + (c.rgb(color[0],color[1],color[2]) + bar())

    return string

def picture(width,height):
    pic = []
    for i in range(height):
        row = []
        for j in range(width):
            if i < 2:
                drops = random()
                if drops > 0.8:
                    row.append([randint(240,255),randint(240,255),randint(240,255)])
                else:
                    row.append([randint(0,10),randint(0,10),randint(0,50)])
            else:
                row.append([randint(0,10),randint(0,10),randint(50,100)])
        pic.append(row)
    return pic

def average(*vecs):
    avg = []
    for i in range(3):
        for v in vecs:
            avg[i] += v[i]
        avg[i] /= len(vecs)


ncols = 100
nrows = 45

chances = [np.geomspace(.3,.95,nrows),np.geomspace(.2,.6,nrows),np.geomspace(.1,.2,nrows)]

def adjust_picture(pic):
    scrambler = random()
    if scrambler > .97:
        shuffle(pic[0])
        shuffle(pic[1])
    for row in range(2,len(pic)):
        for col in range(1,len(pic[row])-1):
            chooser = random()
            if chooser > chances[0][row]:
                pic[row][col] = adjust_clr(pic[row][col],pic[row-randint(1,3)][col])
            elif chooser > chances[1][row]:
                pic[row][col] = adjust_clr(pic[row][col],pic[row][col+1])
            elif chooser > chances[2][row]:
                pic[row][col] = adjust_clr(pic[row][col],pic[row][col-1])
            else:
                pass

def array_picture(array):
    for i in range(len(array)):
        rowstring = ''
        for k in range(len(array[i])):
            if k > 4 and k < (len(array[i]) - 2):
                trip = array[i][k]
                rowstring = rowstring + (c.rgb(trip[0],trip[1],trip[2]) + bar())    
        if i == len(array) - 1:
            print(rowstring)
        else:
            print(rowstring)

print(hide_cursor)
test = picture(ncols,nrows)
while 1:
    adjust_picture(test)
    array_picture(test)
    sleep(.3)
