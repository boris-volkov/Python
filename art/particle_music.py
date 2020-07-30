import sys
import numpy as np
import colors
import time
import sounds
import random

shade = '◡' 
dot = '◉'
star = '◒'
pop = '◬'
pop = '\U000023C1' # this is the totem looking symbol
pop = dot
swap = '⎌'
# these are all of the pre-programmed gestures
gests = [12369,36987,98741,74123,32147,14789,78963,96321,15951,95159,35753,75357,25852,85258,45654,65456,852,654,456,258,159,951,753,357]
scale = sounds.iwato_scale # taken from my sounds package
score = 0 # this should really be called score
margin = ' '*23

class Board(object):
    board = []

    def __init__(self, width, height):
        self.board = [[0]*width for i in range(height)]
        self.width = width
        self.height = height

    def transform(self, d):
        h = self.height
        w = self.width
        R = Board(h, w)
        for i in range(h):
            for j in range(w):
                if d == 'r':
                    R.board[-(j+1)][i] = self.board[i][j]
                if d == 'l':
                    R.board[j][-(i+1)] = self.board[i][j]
                if d == 't':
                    R.board[-(j+1)][-(i+1)] = self.board[i][j]
                if d == 'T':
                    R.board[j][i] = self.board[i][j]
                if d == 'u':
                    R.board[i][-(j+1)] = self.board[i][j]
                if d == 'f':
                    R.board[-(i+1)][j] = self.board[i][j]
                if d == 'md':
                    R.board[i][(j-1)%R.width] = self.board[i][j]
                if d == 'mu':
                    R.board[i][(j+1)%R.width] = self.board[i][j]
                if d == 'ml':
                    R.board[(i-1)%R.height][j] = self.board[i][j]
                if d == 'mr':
                    R.board[(i+1)%R.height][j] = self.board[i][j]
                if d == 'ne':
                    R.board[(i+1)%R.height][(j+1)%R.width] = self.board[i][j]
                if d == 'nw':
                    R.board[(i-1)%R.height][(j+1)%R.width] = self.board[i][j]
                if d == 'se':
                    R.board[(i+1)%R.height][(j-1)%R.width] = self.board[i][j]
                if d == 'sw':
                    R.board[(i-1)%R.height][(j-1)%R.width] = self.board[i][j]
        return R
    
    def transform_drop(self):
        """
        The general animation function that takes 
        care of "dropping" the pieces after a board change
        """
        s = 1 #scale index for the music
        Board.print_board(self, dot)
        print(margin + Board.purple + '\n' + ' '*9, end = '\r')
        bass = scale[:3]
        sounds.pluck(.2,55*random.choice(bass))
        time.sleep(.2)
        while(Board.will_drop(self) == 1):
            for row in self.board:
                for i in range(len(row) - 1):
                    if row[i] == 0 and row[i+1] != 0:
                        row[i] , row[i+1] = row[i+1], row[i]
            Board.print_board(self, dot)
            print(margin + Board.purple + '\n' + ' '*9, end = '\r')
            s += 1
            sounds.play_exp(.1,scale[-s%len(scale)]*110)
            time.sleep(.2)   
        Board.print_board(self, dot)
        print(margin + Board.purple + '\n' + ' '*9, end = '\r')
        return self
    
    def will_drop(self):
        """
        Checks board for whether a drop event must occur
        """
        for row in self.board:
            for i in range(len(row)-1):
                if row[i] == 0 and row[i+1] != 0:
                    return 1
        return 0
                

    def drop(self, row, mark):
        """
        Takes care of dropping a single piece
        
        Not sure if this still needs to exist
        because there is a more general drop 
        function available
        """

        for i in range(len(self.board[row])-1,-1,-1):
          
            print(margin + ' ')
            if self.board[row][i] == 0:
                self.board[row][i] = mark
                Board.print_board(self, dot)
                if i == 0 or not self.board[row][i-1] == 0:
                    print(margin + ' ')
                    Board.print_board(self, star)
                    # i think the print method is to blame for
                    # all these extra empty print lines:
                    # theyre just to bring the cursor down a line
                    # for which i think an ansi escape would work
                    # even better

                    print(margin + Board.purple + '\n' + ' '*9, end = '\r')
                    sounds.play_trap(.3,220*random.choice(scale))
                    time.sleep(0.3)
                    print(margin + ' ')
                    Board.print_board(self, dot)
                    print(margin + '\n', end = '\r')
                    return self
                print(margin + Board.purple + '\n' + ' '*9, end = '\r')
                sounds.play_trap(.1,220*random.choice(scale))
                time.sleep(0.2)
                self.board[row][i] = 0
        return self
    
    def is_four(self):
        pass

    def check_four(self):
        counter = 0
        width = len(self.board[0])
        height = len(self.board)

        # this is the global variable for how many 
        # dots were deleted this round, used elsewhere
        global score
        change = 0
        to_delete = []
        
        # here are separate iterators for horizontal, 
        # vertical and diagonal(two directions) iteration
        
        #verticals
        for row in range(height):
            for col in range(1,width):
                if self.board[row][col] == self.board[row][col-1] and self.board[row][col] != 0:
                    counter += 1
                    try:
                        stopping = self.board[row][col] != self.board[row][col+1]
                    except IndexError:
                        stopping = True
                    if counter >= 3 and ((col == width - 1) or stopping): 
                        change += 1
                        score+=round(2**(counter+1))
                        for d in range(counter+1):
                            to_delete.append((row,col-d))
                else:
                    counter = 0
            counter = 0            
        counter = 0

        #horizontals
        for col in range(width):
            for row in range(1,height):
                if self.board[row][col] == self.board[row-1][col] and self.board[row][col] != 0:
                    counter += 1
                    try:
                        stopping = self.board[row][col] != self.board[row+1][col]
                    except IndexError:
                        stopping = True
                    if counter >= 3 and ((row == height - 1) or stopping): 
                        change += 1
                        score+=round(2**(counter+1))
                        for d in range(counter+1):
                            to_delete.append((row-d,col))
                else:
                    counter = 0
            counter = 0           
        counter = 0

        # one direction of diagonals
        for a in range(height - 3):
            for i in range(width - 3):
                for j in range(min(height-a-1, width-i-1)):
                    border = False
                    try:
                        self.board[a+j+2][i+j+2] == None
                    except IndexError:
                        border = True
                    if self.board[a + j][i + j] == self.board[a + j + 1][i + 1 + j] and self.board[a + j][i + j] != 0:
                        counter += 1
                        if counter >= 3: 
                            if border or (self.board[a+j+1][i+j+1] != self.board[a+j+2][i+j+2]):
                                change += 1
                                score+=round(2**(counter+1))
                                for d in range(counter+1):
                                    to_delete.append((a+j+1-d,i+j+1-d))
                    else:
                        counter = 0
                counter = 0
            counter = 0            
        counter = 0

        # other direction of diagonals
        for a in range(height - 3):
            for i in range(3, width):
                for j in range(min(height-a-1, i)):
                    border = False
                    try:
                        self.board[a+j+2][i-j-2] == None
                    except IndexError:
                        border = True
                    if self.board[a+j][i-j] == self.board[a+j+1][i-j-1] and self.board[a+j][i-j] != 0:
                        counter += 1
                        if counter >= 3: 
                            if border or (self.board[a+j+1][i-j-1] != self.board[a+j+2][i-j-2]):
                                change += 1
                                score+=round(2**(counter+1))
                                for d in range(counter+1):
                                    to_delete.append((a+j+1-d,i-j-1+d))
                    else:
                        counter = 0
                counter = 0
            counter = 0
        counter = 0

        # rectangle
        # every rectangle is made up of these 2x2 squares
        square_set = set()
        for i in range(height - 1):
            for j in range(width -1):
                if self.board[i][j] != 0:
                    if self.board[i][j]==self.board[i+1][j]==self.board[i][j+1]==self.board[i+1][j+1]:
                        square_set.add((i,j))
                        square_set.add((i+1,j))
                        square_set.add((i,j+1))
                        square_set.add((i+1,j+1))
                        change += 1 
        if square_set:
            score += 2**len(square_set)
        for s in square_set:
            to_delete.append(s)

        for e in to_delete:
            self.board[e[0]][e[1]] = 'd'
        if to_delete:
            Board.print_board(self, dot)
            print(margin + ' ')
            sounds.pluck(.1,110*scale[0])
            sounds.pluck(.1,110*scale[1])
            sounds.pluck(.3,110*random.choice(scale))
            time.sleep(.5)
        for e in to_delete:
            self.board[e[0]][e[1]] = 0
        return (self, change > 0, score)

    def is_space(self,x):
        return self.board[x][-1] == 0

    #color scheme is very important
    blue = colors.rgb(70,70,200)
    yellow = colors.rgb(200,200,50)
    purple = colors.rgb(200,0,70)
    red = colors.rgb(250, 50,150)
    green = colors.rgb(0,100,50)
    white = colors.rgb(255,220,180)
    line_color = colors.rgb(255,255,255)
    
    
    # these are the circled numbers under the columns
    base_nums = ['\U00002460', '\U00002461', '\U00002462', '\U00002463', '\U00002464', '\U00002465', '\U00002466', '\U00002467', '\U00002468', '\U00002469', '\U0000246a', '\U0000246b', '\U0000246c', '\U0000246d', '\U0000246e', '\U0000246f', '\U00002470', '\U00002471', '\U00002472', '\U00002473',]
    

    def print_board(self,dot):
        for i in range(1,len(self.board[0])+1):
            rowstring = ''
            for j in range(len(self.board)):
                c = self.board[j][-i]
                if c == 'x':
                    rowstring = rowstring + Board.blue + dot
                if c == 'o':
                    rowstring = rowstring + Board.yellow + dot
                if c == 't':
                    rowstring = rowstring + Board.red + dot
                if c == 'u':
                    rowstring = rowstring + Board.green + dot
                if c == 'd':
                    rowstring = rowstring + Board.line_color + pop
                elif c == 0:
                    rowstring = rowstring + Board.purple +shade
            print(margin + rowstring + Board.purple)
        print(margin, end = '')
        for i in range(len(self.board)):
            print(Board.base_nums[i%len(Board.base_nums)], end = '')
        print(colors.rgb(250,250,250) + '\n'+margin +'\U000023C1'+  str(score) +Board.purple, end = '')

if __name__ == '__main__':
    score = 0


    clrs = [Board.blue, Board.yellow, Board.red, Board.green]
    players = int(sys.argv[3])
    tokens = ['x', 'o', 't', 'u']

    # limit rand fill to match number of colors
    rand_fill = ['x','o','t','u',0]
    rand_fill = [e for i,e in enumerate(rand_fill) if i < players]
    rand_fill.append(0) # an egg
    print(margin + colors.hide_cursor)
    height = int(sys.argv[1])
    width = int(sys.argv[2]) #these are the apparent height and width on screen
    B = Board(height,width)
    
    #initialize random board
    for row in range(height):
        for col in range(width):
            B.board[row][col] = random.choice(rand_fill)
    B = Board.transform_drop(B)
    while (Board.check_four(B)[1]):
        B,a,c = Board.check_four(B)
        B = Board.transform_drop(B)

    Board.print_board(B,dot)
    print(' ') 

    while ( Board.check_four(B)[1]):
        B = Board.check_four(B)[0]
        B = Board.transform_drop(B)
    rounds = 1
    alive = True
    while alive:
        i = rounds
        sys.stdout.flush()
        p = input(margin + Board.purple + swap + ' : ')

        if p == 's':
            alive = False
            break

        while not (p.isnumeric()) or ((int(p) > B.width or int(p) < 1) and 
                (int(p) not in gests)) or (int(p) < 100 and 
                        not Board.is_space(B,int(p)-1)):
            Board.print_board(B,dot)
            sounds.play_sawtooth(.15,110)
            print(margin + ' ')
            p = input(margin + Board.purple + swap + ' : ')
        
            
        if p.isnumeric():
            p = int(p)
            if p in gests:
                if p == 12369 or p == 36987 or p == 98741 or p == 74123:
                    B = Board.transform(B, 'r')
                if p == 32147 or p == 14789 or p == 78963 or p == 96321:
                    B = Board.transform(B, 'l')
                if p == 15951 or p == 95159:
                    B = Board.transform(B, 't')
                if p == 35753 or p == 75357:
                    B = Board.transform(B, 'T')
                if p == 25852 or p == 85258:
                    B = Board.transform(B, 'u')
                if p == 45654 or p == 65456:
                    B = Board.transform(B, 'f')
                if p == 852:
                    B = Board.transform(B, 'md')
                if p == 654:
                    B = Board.transform(B, 'ml')
                if p == 456:
                    B = Board.transform(B, 'mr')
                if p == 258:
                    B = Board.transform(B, 'mu')
                if p == 159:
                    B = Board.transform(B, 'ne')
                if p == 951:
                    B = Board.transform(B, 'sw')
                if p == 357:
                    B = Board.transform(B, 'nw')
                if p == 753:
                    B = Board.transform(B, 'se')
                B = Board.transform_drop(B)
        available = [i for i in range(B.width) if Board.is_space(B,i)]
        if available:
            R = random.choice(available)        
            B = Board.drop(B, R, tokens[i%players])
        while ( Board.check_four(B)[1]):
            B,a,c = Board.check_four(B)
            B = Board.transform_drop(B)

        rounds += 1

    
    print(margin + colors.clear_screen)
    _ = input(Board.purple + 'thank you for playing')
    print(margin + colors.stop_blink)
    print(margin + colors.clear_screen)
