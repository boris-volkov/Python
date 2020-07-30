import colors as c
from random import random, randint
from time import sleep
from colors import show_cursor, hide_cursor

bar = '\U00002588'

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
        string = string + (c.rgb(color[0],color[1],color[2]) + bar)

    return string

def picture(width,height):
    pic = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append([randint(100,200),randint(0,100),randint(200,255)])
        pic.append(row)
    return pic

def average(*vecs):
    avg = []
    for i in range(3):
        for v in vecs:
            avg[i] += v[i]
        avg[i] /= len(vecs)

def adjust_picture(pic):
    for row in range(1,len(pic)-1):
        for col in range(1,len(pic[row])-1):
            chooser = randint(1,20)
            if chooser > 7:
                pic[row][col] = adjust_clr(pic[row][col],pic[row+1][col])
            elif chooser > 5:
                pic[row][col] = adjust_clr(pic[row][col],pic[row+1][col-1])
            elif chooser > 3:
                pic[row][col] = adjust_clr(pic[row][col],pic[row][col-1])
            elif chooser > 2:
                pic[row][col] = adjust_clr(pic[row][col],pic[row][col+1])

def array_picture(array):
    for i in range(len(array)):
        rowstring = ''
        for k in range(len(array[i])):
            if k > 4 and k < (len(array[i]) - 2):
                trip = array[i][k]
                rowstring = rowstring + (c.rgb(trip[0],trip[1],trip[2]) + bar)    
        if i == len(array) - 1:
            print(rowstring, end = '')
        else:
            print(rowstring)

print(hide_cursor)
test = picture(91,46)
while 1:
    adjust_picture(test)
    array_picture(test)
    sleep(.3)
