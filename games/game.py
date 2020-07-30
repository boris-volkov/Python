from getch import getch
import colors
import random
import time

size = 8 



# stuff for printing
dot = '◉'
black = colors.rgb(0,0,0)
white = colors.rgb(255,255,255)
cyan = colors.cyan
red = colors.red
magenta = colors.rgb(250,0,250)
yellow = colors.yellow
frog = '☻'
block = '◯'

print(colors.hide_cursor)

def make_grid(n):
    return [[0]*n for i in range(n)]

grid = make_grid(size)

"""
for i in range(size//2):
    for j in range(size//2):
        grid[i][j] = 0
for i in range(size//2):
    for j in range(size//2,size):
        grid[i][j] = 1
for i in range(size//2,size):
    for j in range(size//2,size):
        grid[i][j] = 2
for i in range(size//2,size):
    for j in range(size//2):
        grid[i][j] = 3
"""

grid[0][0] = 1

def move_guy(grid, way):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if way == 'up' and grid[(i-1)%n][j] == 0 :
                    grid[i][j], grid[(i-1)%n][j] = 0,1
                    return grid
                if way == 'down' and grid[(i+1)%n][j] == 0 :  
                    grid[i][j], grid[(i+1)%n][j] = 0,1
                    return grid
                if way == 'left' and grid[i][(j-1)%n] == 0 :
                    grid[i][j], grid[i][(j-1)%n] = 0,1
                    return grid
                if way == 'right' and grid[i][(j+1)%n] == 0 :
                    grid[i][j], grid[i][(j+1)%n] = 0,1
                    return grid

def mobius_shift(grid, way):
    _new_ =  make_grid(size)
    if way == 'right':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[i][(j-1)%size]
        for i in range(size):
            _new_[i][0] = grid[-((i+1)%size)][-1]
        return _new_

    if way == 'left':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[i][(j+1)%size]
        for i in range(size):
            _new_[i][-1] = grid[-((i+1)%size)][0]
        return _new_
    
    if way == 'up':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[(i+1)%size][j]
        for i in range(size):
            _new_[-1][i] = grid[0][-((i+1)%size)]
        return _new_

    if way == 'down':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[(i-1)%size][j]
        for i in range(size):
            _new_[0][i] = grid[-1][-((i+1)%size)]
        return _new_

def torus_shift(grid, way):
    _new_ =  make_grid(size)
    if way == 'right':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[i][(j-1)%size]
        return _new_

    if way == 'left':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[i][(j+1)%size]
        return _new_
    
    if way == 'up':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[(i+1)%size][j]
        return _new_

    if way == 'down':
        for i in range(size):
            for j in range(size):
                _new_[i][j] = grid[(i-1)%size][j]
        return _new_


base_nums = ['\U00002460', '\U00002461', '\U00002462', '\U00002463', '\U00002464', '\U00002465', '\U00002466', '\U00002467', '\U00002468', '\U00002469', '\U0000246a', '\U0000246b', '\U0000246c', '\U0000246d', '\U0000246e', '\U0000246f', '\U00002470', '\U00002471', '\U00002472', '\U00002473',]

board_colors = [black,yellow,cyan,red,magenta,yellow]
board_colors = [colors.rgb(250,250,0),
                colors.rgb(50,150,255),
                colors.rgb(255,80,80),
                colors.rgb(50,205,55)]



#board_colors = [white, black, white, black]

def print_grid(grid):
    for row in grid:
        for e in row:
            print(yellow if e == 1 else black, end = '')
            print(frog if e == 1 else block, end = '')
        print('')
    print('')


def play_auto(grid):
    key = random.choice(['A','D','C','B','d','a','w','s'])
    print_grid(grid)
    if key == 'A':
        grid = torus_shift(grid,'up')
        print_grid(grid)
    elif key == 'D':
        grid = torus_shift(grid,'left')
        print_grid(grid)
    elif key == 'C':
        grid = torus_shift(grid,'right')
        print_grid(grid)
    elif key == 'B':
        grid = torus_shift(grid,'down')
        print_grid(grid)

    elif key == 'd' or key == '6':
        grid = mobius_shift(grid,'right')
        print_grid(grid)
    elif key == 'a' or key == '4':
        grid = mobius_shift(grid,'left')
        print_grid(grid)
    elif key == 'w' or key == '8':
        grid = mobius_shift(grid, 'up' )
        print_grid(grid)
    elif key == 's' or key == '2' or key == '5':
        grid = mobius_shift(grid, 'down' )
        print_grid(grid)
    return grid


def play(grid):
    print_grid(grid)
    key = getch()[-1]
    if key == 'A':
        grid = move_guy(grid,'up')
        print_grid(grid)
    elif key == 'D':
        grid = move_guy(grid,'left')
        print_grid(grid)
    elif key == 'C':
        grid = move_guy(grid,'right')
        print_grid(grid)
    elif key == 'B':
        grid = move_guy(grid,'down')
        print_grid(grid)

    elif key == 'd' or key == '6':
        grid = mobius_shift(grid,'right')
        print_grid(grid)
    elif key == 'a' or key == '4':
        grid = mobius_shift(grid,'left')
        print_grid(grid)
    elif key == 'w' or key == '8':
        grid = mobius_shift(grid, 'up' )
        print_grid(grid)
    elif key == 's' or key == '2' or key == '5':
        grid = mobius_shift(grid, 'down' )
        print_grid(grid)
    return grid

#while 1:
#    grid = play_auto(grid)
#    time.sleep(1)

while 1:
    grid = play(grid)
