import sys
import numpy as np
import colors
import time
import sounds

shade = '◡' 
dot = '◉'
star = '◬'
star = '◒'

class Board(object):
    board = []

    def __init__(self, width, height):
        #self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.board = [[0]*width for i in range(height)]
        

    def drop(self, row, mark):
        for i in range(len(self.board[row])-1,-1,-1):
          
            print(' ')
            if self.board[row][i] == 0:
                self.board[row][i] = mark
                Board.print_board(self, dot)
                if i == 0 or not self.board[row][i-1] == 0:
                    Board.print_board(self, star)
                    print(Board.purple + '\n' + ' '*9, end = '\r')
                    sounds.play_trap(.3,55*sounds.octaves(sounds.insen_scale,4)[i])
                    time.sleep(0.3)
                    print(' ')
                    Board.print_board(self, dot)
                    print('\n', end = '\r')
                    return self
                print(Board.purple + '\n' + ' '*9, end = '\r')
                sounds.play_trap(.1,sounds.octaves(sounds.insen_scale,4)[i]*55)
                time.sleep(0.1)
                self.board[row][i] = 0
        return self
    
    
    def check_four(self):
        counter = 0
        width = len(self.board[0])
        height = len(self.board)
       
        #verticals
        for row in range(height):
            for col in range(1,width):
                if self.board[row][col] == self.board[row][col-1] and self.board[row][col] != 0:
                    counter += 1
                    if counter == 3:
                        return 1
                else:
                    counter = 0
            counter = 0
        counter = 0

        #horizontals
        for col in range(width):
            for row in range(1,height):
                if self.board[row][col] == self.board[row-1][col] and self.board[row][col] != 0:
                    counter += 1
                    if counter == 3:
                        return 1
                else:
                    counter = 0
            counter = 0
        counter = 0
 
        #left to right diagonals across top
        for a in range(height - 3):
            for i in range(width - 3):
                for j in range(3):
                    if self.board[a + j][i + j] == self.board[a + j + 1][i + 1 + j] and self.board[a + j][i + j] != 0:
                        counter += 1
                        if counter == 3:
                            return 1
                    else:
                        counter = 0
                counter = 0
        counter = 0
    
        #left to right diagonals across top
        for a in range(height - 3):
            for i in range(3, width):
                for j in range(3):
                    if self.board[a + j][i - j] == self.board[a + j + 1][i - j - 1] and self.board[a + j][i - j] != 0:
                        counter += 1
                        if counter == 3:
                            return 1
                    else:
                        counter = 0
                counter = 0
        return 0

    def is_space(self,x):
        return self.board[x][-1] == 0


    blue = colors.rgb(70,70,250)
    yellow = colors.rgb(250,250,50)
    purple = colors.rgb(150,0,50)
    red = colors.rgb(250, 50,150)
    green = colors.rgb(50,250,50)
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
                elif c == 0:
                    rowstring = rowstring + Board.purple +shade
            print(rowstring + Board.purple)
        for i in range(len(self.board)):
            print(Board.base_nums[i], end = '')
        print('\n'+Board.purple, end = '\r')

if __name__ == '__main__':
    print(colors.hide_cursor)
    height = int(sys.argv[1])
    width = int(sys.argv[2]) #these are the apparent height and width on screen
    B = Board(height,width)
    Board.print_board(B,dot)
    if int(sys.argv[3]) == 4:
        print(colors.rgb(210,220,255) + '\U000023C1 ' + Board.blue + dot+' ' + 
            Board.yellow + dot + Board.red + ' ' +  dot + Board.green + ' ' + dot)
    if int(sys.argv[3]) == 3:
        print(colors.rgb(210,220,255) + '\U000023C1 ' + Board.blue + dot+' ' + 
            Board.yellow + dot + Board.red + ' ' +  dot)
    
    if int(sys.argv[3]) == 2:
        print(colors.rgb(210,220,255) + '\U000023C1 ' + Board.blue + dot+' ' + 
            Board.yellow + dot)


    while Board.check_four(B) == 0:
        clrs = [Board.blue, Board.yellow, Board.red, Board.green]
        tokens = ['x', 'o', 't', 'u']
        for i in range(int(sys.argv[3])):
            p1 = input(clrs[i]+' ' + dot + ' : ')
            while not p1.isnumeric() or (int(p1) > width or int(p1) < 1) or not Board.is_space(B,int(p1)-1):
                Board.print_board(B,dot)
                sounds.play_sawtooth(.15,110)
                print(colors.blink + colors.rgb(250,50,50) + 'not valid'+colors.stop_blink)
                p1 = input(clrs[i] +' ' +' ' + dot + ' : ')
            row = int(p1) - 1
            B = Board.drop(B, row, tokens[i])
            if Board.check_four(B) == 1:
                print(colors.blink + clrs[i] + ' ' + dot + ' wins', end = '')
                sounds.trap(.2,220)
                sounds.trap(.2,440)
                break
    _ = input()
    print(colors.stop_blink)
    print(colors.clear_screen)
