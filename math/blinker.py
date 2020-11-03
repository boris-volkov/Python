import colors
import time
import sys

dot = '◉'
black = colors.rgb(0,0,0)
red = colors.yellow
yellow = colors.yellow
margin = ' '*6

def grid(width = 10, counter = 0,rate = 0.05):
    print(colors.hide_cursor)
    while 1:
        print('\n' + margin, end = '')
        for i in range(1,width**2+1):
            print('', end = ' ')
            if counter % i == 0 and i%width == 0:
                print(red + dot)
                print(margin, end = '')
            elif counter % i == 0:
                print(red + dot ,end = '')
            elif i % width == 0:
                print(black + dot)
                print(margin, end = '')
            else:
                print(black + dot, end = '')
        print(yellow + str(counter))
        time.sleep(rate)
        print(colors.clear_screen)
        counter += 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        grid(int(sys.argv[1]))
