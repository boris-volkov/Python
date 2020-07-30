import sys
import numpy as np
import colors
import time
import sounds

shade = '◡' 
dot = '◉'
star = '◒'
gests = [12369,36987,98741,74123,32147,14789,78963,96321,15951,95159,35753,75357,25852,85258,45654,65456,852,654,456,258,159,951,753,357]
scale = sounds.iwato_scale

margin = '      '

class Board(object):
    board = []

    def __init__(self, width, height):
        self.board = [[0]*width for i in range(height)]
        self.width = width
        self.height = height

    def rotate(self, d):
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
    
    def rotate_drop(self):
        s = 1
        Board.print_board(self, dot)
        sounds.play_trap(.1,sounds.octaves(scale,3)[-s]*55)
        print(margin + Board.purple + '\n' + ' '*9, end = '\r')
        time.sleep(.2)
        while(Board.will_drop(self) == 1):
            for row in self.board:
                for i in range(len(row) - 1):
                    if row[i] == 0 and row[i+1] != 0:
                        row[i] , row[i+1] = row[i+1], row[i]
            Board.print_board(self, dot)
            print(margin + Board.purple + '\n' + ' '*9, end = '\r')
            s += 1
            sounds.play_trap(.1,sounds.octaves(scale,3)[-s]*55)
            time.sleep(.2)
        return self
    
    def will_drop(self):
        for row in self.board:
            for i in range(len(row)-1):
                if row[i] == 0 and row[i+1] != 0:
                    return 1
        return 0
                

    def drop(self, row, mark):
        for i in range(len(self.board[row])-1,-1,-1):
          
            print(margin + ' ')
            if self.board[row][i] == 0:
                self.board[row][i] = mark
                Board.print_board(self, dot)
                if i == 0 or not self.board[row][i-1] == 0:
                    Board.print_board(self, star)
                    print(margin + Board.purple + '\n' + ' '*9, end = '\r')
                    sounds.play_trap(.3,110*sounds.octaves(scale,3)[i])
                    time.sleep(0.3)
                    print(margin + ' ')
                    Board.print_board(self, dot)
                    print(margin + '\n', end = '\r')
                    return self
                print(margin + Board.purple + '\n' + ' '*9, end = '\r')
                sounds.play_trap(.1,sounds.octaves(scale,3)[i]*110)
                time.sleep(0.2)
                self.board[row][i] = 0
        return self
    
    
    def check_four(self):
        counter = 0
        winner = 'a'
        width = len(self.board[0])
        height = len(self.board)
        winners = []

        #verticals
        for row in range(height):
            for col in range(1,width):
                if self.board[row][col] == self.board[row][col-1] and self.board[row][col] != 0:
                    counter += 1
                    if counter == 3:
                        winners.append(self.board[row][col])
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
                        winners.append(self.board[row][col])
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
                            winners.append(self.board[a+j][i+j])
                    else:
                        counter = 0
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
                            winners.append(self.board[a+j][i-j])
                    else:
                        counter = 0
                counter = 0
            counter = 0
        counter = 0
        return winners

    def is_space(self,x):
        return self.board[x][-1] == 0


    blue = colors.rgb(70,70,250)
    yellow = colors.rgb(250,250,50)
    purple = colors.rgb(200,0,70)
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
            print(margin + rowstring + Board.purple)
        print(margin, end = '')
        for i in range(len(self.board)):
            print(Board.base_nums[i], end = '')
        print(margin + '\n'+Board.purple, end = '\r')

if __name__ == '__main__':
    print(margin + colors.hide_cursor)
    height = int(sys.argv[1])
    width = int(sys.argv[2]) #these are the apparent height and width on screen
    B = Board(height,width)
    Board.print_board(B,dot)
    if int(sys.argv[3]) == 4:
        print(margin + colors.rgb(210,220,255) + '\U000023C1 ' + Board.blue + dot+ 
            Board.yellow + dot + Board.red + dot + Board.green + dot)
    if int(sys.argv[3]) == 3:
        print(margin + colors.rgb(210,220,255) + '\U000023C1 ' + Board.blue + dot+ 
            Board.yellow + dot + Board.red +  dot)
    if int(sys.argv[3]) == 2:
        print(margin + colors.rgb(210,220,255) + '\U000023C1 ' + Board.blue + dot+' ' + 
            Board.yellow + dot)



    #while len(Board.check_four(B)) == 0:
    while 1:
        clrs = [Board.blue, Board.yellow, Board.red, Board.green]
        tokens = ['x', 'o', 't', 'u']
        for i in range(int(sys.argv[3])):
            p = input(margin + clrs[i]+dot + ' : ')
            if p == 'r' or p == 'l':
                B = Board.rotate(B, p)
                B = Board.rotate_drop(B)
                if len(Board.check_four(B)) > 0:
                    for t in Board.check_four(B):
                        winning_index = tokens.index(t)
                        print(margin + colors.blink + clrs[winning_index] + ' ' + dot + ' wins', end = '')
                    break
                continue

            while not (p.isnumeric()) or ((int(p) > B.width or int(p) < 1) and (int(p) not in gests)) or (int(p) < 100 and not Board.is_space(B,int(p)-1)):
                Board.print_board(B,dot)
                sounds.play_sawtooth(.15,110)
                #print(margin + colors.blink + colors.rgb(250,50,50) + 'not valid'+colors.stop_blink)
                print(margin + ' ')
                p = input(margin + clrs[i] +' ' +' ' + dot + ' : ')
            

            if p.isnumeric():
                p = int(p)
                if p in gests:
                    if p == 12369 or p == 36987 or p == 98741 or p == 74123:
                        B = Board.rotate(B, 'r')
                    if p == 32147 or p == 14789 or p == 78963 or p == 96321:
                        B = Board.rotate(B, 'l')
                    if p == 15951 or p == 95159:
                        B = Board.rotate(B, 't')
                    if p == 35753 or p == 75357:
                        B = Board.rotate(B, 'T')
                    if p == 25852 or p == 85258:
                        B = Board.rotate(B, 'u')
                    if p == 45654 or p == 65456:
                        B = Board.rotate(B, 'f')
                    if p == 852:
                        B = Board.rotate(B, 'md')
                    if p == 654:
                        B = Board.rotate(B, 'ml')
                    if p == 456:
                        B = Board.rotate(B, 'mr')
                    if p == 258:
                        B = Board.rotate(B, 'mu')
                    if p == 159:
                        B = Board.rotate(B, 'ne')
                    if p == 951:
                        B = Board.rotate(B, 'sw')
                    if p == 357:
                        B = Board.rotate(B, 'nw')
                    if p == 753:
                        B = Board.rotate(B, 'se')
                    B = Board.rotate_drop(B)
                    """
                    if len(Board.check_four(B)) > 0:
                        for t in Board.check_four(B):
                            winning_index = tokens.index(t)
                            print(margin + colors.blink + clrs[winning_index] + ' ' + dot + ' wins', end = '')
                            sounds.pluck(.2,220)
                            sounds.pluck(.4,440)
                        break
                    continue
                    """
            if (p <= B.width and p > 0):        
                row = p - 1
                B = Board.drop(B, row, tokens[i])
            """
            if len(Board.check_four(B)) > 0:
                print(margin + colors.blink + clrs[i] + ' ' + dot + ' wins', end = '')
                sounds.pluck(.2,220)
                sounds.pluck(.4,440)
                break
            """
    _ = input()
    print(margin + colors.stop_blink)
    print(margin + colors.clear_screen)
