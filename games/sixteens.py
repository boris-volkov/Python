from getch import getch
import colors
import random
import time

size = 4



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
block = '☗'
block = '█'

print(colors.hide_cursor)

def make_grid(n):
    return [[0]*n for i in range(n)]

grid = make_grid(size)


for i in range(size):
    for j in range(size):
        grid[i][j] = i*size + j

def move_guy(grid, way):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if way == 'up' and grid[(i-1)%n][j] == 0 :
                    grid[i][j], grid[(i-1)%n][j] = 0,1
                    return
                if way == 'down' and grid[(i+1)%n][j] == 0 :  
                    grid[i][j], grid[(i+1)%n][j] = 0,1
                    return
                if way == 'left' and grid[i][(j-1)%n] == 0 :
                    grid[i][j], grid[i][(j-1)%n] = 0,1
                    return
                if way == 'right' and grid[i][(j+1)%n] == 0 :
                    grid[i][j], grid[i][(j+1)%n] = 0,1
                    return

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
board_colors = [colors.bg_rgb(250,250,0),
                colors.bg_rgb(50,150,255),
                colors.bg_rgb(255,80,80),
                colors.bg_rgb(50,205,55)]

#board_colors = [white, black, white, black]

margin = ' '*5
white = colors.rgb(255,255,255)
black = colors.rgb(0,0,0)

def print_grid(grid):
    for row in grid:
        print(margin + black, end = '')
        for e in row:
            print(board_colors[e%size] + base_nums[e], end = '')
        print(colors.reset)
    print('\n')


left = '◀' 
right = '▶' 
up = '▲'
down = '▼'

def arrow_string(way):
    return ''
    if way == 'left':
        return margin + white + left + black + up + down + right 
    if way == 'up':
        return margin + black + left +white +  up +black +  down + right 
    if way == 'down':
        return margin + black + left + up + white + down + black + right 
    if way == 'right':
        return margin + black + left + up + down + white + right + black 

def play_auto(grid):
    print('shuffling')
    key = random.choice(['d','a','w','s'])
    print_grid(grid)
    if key == 'A':
        grid = torus_shift(grid,'up')
        print_grid(grid)
        print(arrow_string('up'))
    elif key == 'D':
        grid = torus_shift(grid,'left')
        print_grid(grid)
        print(arrow_string('left'))
    elif key == 'C':
        grid = torus_shift(grid,'right')
        print_grid(grid)
        print(arrow_string('right'))
    elif key == 'B':
        grid = torus_shift(grid,'down')
        print_grid(grid)
        print(arrow_string('down'))

    elif key == 'd' or key == '6':
        grid = mobius_shift(grid,'right')
        print_grid(grid)
        print(arrow_string('right'))
    elif key == 'a' or key == '4':
        grid = mobius_shift(grid,'left')
        print_grid(grid)
        print(arrow_string('left'))
    elif key == 'w' or key == '8':
        grid = mobius_shift(grid, 'up' )
        print_grid(grid)
        print(arrow_string('up'))
    elif key == 's' or key == '2' or key == '5':
        grid = mobius_shift(grid, 'down' )
        print_grid(grid)
        print(arrow_string('down'))
    return grid


def play(grid):
    print_grid(grid)
    key = getch()[-1]

    print_grid(grid)
    if key == 'A':
        grid = torus_shift(grid,'up')
        print_grid(grid)
        print(arrow_string('up'))
    elif key == 'D':
        grid = torus_shift(grid,'left')
        print_grid(grid)
        print(arrow_string('left'))
    elif key == 'C':
        grid = torus_shift(grid,'right')
        print_grid(grid)
        print(arrow_string('right'))
    elif key == 'B':
        grid = torus_shift(grid,'down')
        print_grid(grid)
        print(arrow_string('down'))

    elif key == 'd' or key == '6':
        grid = mobius_shift(grid,'right')
        print_grid(grid)
        print(arrow_string('right'))
    elif key == 'a' or key == '4':
        grid = mobius_shift(grid,'left')
        print_grid(grid)
        print(arrow_string('left'))
    elif key == 'w' or key == '8':
        grid = mobius_shift(grid, 'up' )
        print_grid(grid)
        print(arrow_string('up'))
    elif key == 's' or key == '2' or key == '5':
        grid = mobius_shift(grid, 'down' )
        print_grid(grid)
        print(arrow_string('down'))
    return grid

"""

#for competition mode
for i in range(1000):
    grid = play_auto(grid)
    time.sleep(1)
"""
while 1:
    grid = play(grid)
