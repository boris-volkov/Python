import random, time, sys, colors

PICWIDTH = 62
PICHEIGHT = 33
CENTER = (PICHEIGHT//2, PICWIDTH//2)
BLOCK = '█'
EMPTY = ' '

picture = [[0]*PICWIDTH for _ in range(PICHEIGHT)]


def in_circle(point, center, radius):
    x,y = point
    X,Y = center
    return (X-x)**2 + (Y-y)**2 < radius**2


for i in range(PICHEIGHT):
    for j in range(PICWIDTH):
        picture[i][j] += in_circle((i,j) , CENTER, 5)

def shade(value):
    
    tup = (min(value//3,255), min(value//1,255), min(value//2,255))
    return tup

    
def print_picture(picture):      
    string = ''
    for i in range(PICHEIGHT):
        for j in range(PICWIDTH):
                string = string + colors.rgb(*shade(abs(picture[i][j]))) + BLOCK
    print('\x1bc')
    print(string)

def go(_from):
    a,b = _from
    a += random.randint(-1,1)
    if a < 0: a = 0
    if a >= PICHEIGHT: a = PICHEIGHT - 1
    b += random.randint(-1,1)
    if b < 0: b = 0
    if b >= PICWIDTH: b = PICWIDTH - 1
    return (a,b)

from threading import Thread

def go_thread(pt):
    return Thread(Target = go(pt))

def scatter(pic):
    while 1:
        for i in range(PICHEIGHT):
            for j in range(PICWIDTH):
                if picture[i][j] != 0:
                    picture[i][j] += random.randint(-10,10)
                if picture[i][j] > 255:
                    picture[i][j] = round(picture[i][j] * random.random())
                if picture[i][j] > 100:
                    x,y = go((i,j))
                    picture[x][y] += random.randint(-10,20)
        print_picture(picture)
        time.sleep(.5)

scatter(picture)
