import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
from random import random

def myround(x, base=5):
    return base * round(x/base)

def difference(pic1, pic2):
    diff = pic2 + -1*pic1 
    return diff

def adjust_clr(triple, target):
    return np.array(triple + random()*(target + -1*triple),dtype = np.uint8)

def adjust_picture(P):
    title = P
    for i in range(150):
        current_img = Image.open(title)
        pic = np.array(current_img)
        for row in range(1,len(pic)-1):
            for col in range(1,len(pic[row])-1):
                chooser = random()
                ranges = np.linspace(0,1,7)
                if chooser < ranges[0]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row+1][col])
                elif chooser < ranges[1]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row+1][col+1])
                elif chooser <  ranges[2]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row][col+1])
                elif chooser <  ranges[3]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row-1][col+1])
                elif chooser <  ranges[4]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row-1][col])
                elif chooser <  ranges[5]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row-1][col-1])
                elif chooser <  ranges[6]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row][col-1])
                elif chooser <  ranges[7]:
                    pic[row][col] = adjust_clr(pic[row][col],pic[row+1][col+1])
        to_save = Image.fromarray(pic)
        title = ('frame' + str(i).zfill(4)+ '.png')
        to_save.save(title)
        print(title + ' : written')
         

def transition(start, path, frames):
    for i in range(frames):
        current = np.array(start + (i/frames)*path,dtype=np.uint8)
        to_save = Image.fromarray(current)
        to_save.save('frame' + str(i).zfill(4)+ '.jpg')


if __name__ == '__main__':
    start_img = Image.open(sys.argv[1])
    start = np.array(start_img)
    if len(sys.argv) < 3:
        adjust_picture(sys.argv[1])
    finish_img= Image.open(sys.argv[2])
    finish= np.array(finish_img)
    diff = difference(start, finish)
    print(diff)
    transition(start,diff,10)
