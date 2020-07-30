import random, os
import getpass
import pickle
import time
import effects as q
import sys
from colors import rgb, bg_rgb, hide_cursor

margin = '       '
cyan        = rgb(50,180,210)
yellow      = rgb(210,180,110)
green       = rgb(50,240,120)
red         = '\u001b[91m'
bold        = '\u001b[1m'
clear       = '\u001b[0m'
screen      = '\033[2J'

print(hide_cursor)

def make_string(a):
    upper = a.top
    lower = a.bot
    answer= a.ans

    uLen = len(str(upper))
    lLen = len(str(lower))
    aLen = len(str(answer))
    digits = max(uLen, lLen, aLen-2)

    return(cyan + margin + ' '*2 + f'{str(upper):>{digits}}' + '\n' +
              margin + yellow + bold + 'x'  + clear + cyan +
                       ' '*1  +  f'{str(lower):>{digits}}'   + '\n' +
              margin + '-'*(2 + digits)                      + '\n' +
              margin + ' '*(2 + digits - aLen)
          )


class Problem(object):
    def __init__(self, a, b, opp):
        self.top = a
        self.bot = b
        self.ans = opp(a,b)
        self.avg = 10

    def update_avg(self, time):
        self.avg = (self.avg*2 + time)/3
    
    def next_problem(self):
        if self.top > self.bot:
            self.bot += 1
        else:
            self.top += 1
            self.bot = 2
        self.ans = self.top*self.bot
    
    def __str__(self):
        digits = max(len(str(self.top)), len(str(self.bot)), len(str(self.ans)))
        return(cyan + margin + ' '*2 + f'{str(self.top):>{digits}}' + '\n' +
                  margin + yellow + bold + 'x'  + clear + cyan +
                           ' '*1  +  f'{str(self.bot):>{digits}}'   + '\n' +
                  margin + '-'*(2 + digits)                      + '\n' +
                  margin + ' '*(2 + digits - len(str(self.ans)))
              )

    def __repr__(self):
        return '{}x{}={}, average time: {}'.format(self.top, self.bot, self.ans, self.avg )

class Player(object):
    def __init__(self,name, limit):
        self.name = name
        self.list = Player.generate_probs(limit)
        self.biggest = Problem(limit-1, limit-1) 
        self.mastered = 0
    def __iter__(self):
        return iter(self.list)
    def __repr__(self):
        for i in self:
            print(i)
            time.sleep(1)
    def generate_probs(limit):
        table = []
        for i in range(2,limit):
            for j in range(i,limit):
                table.append( Problem(j, i, int.__mul__) )
        return table



def progress_bar(n):
    w = os.get_terminal_size()[0]
    bars = ['' , '\U0000258F','\U0000258E',
            '\U0000258D', '\U0000258C', '\U0000258B', 
            '\U0000258A' , '\U00002589', '\U00002588']
    progress = bars[-1]*int(n//(1/w))
    rem = (n/(1/w))-(n//(1/w))
    progress = progress +  bars[int(rem*8//1)]
    return progress

def times(player, how_many):
    done = 0

    def ask(a):
        user_guess = ""
        while not user_guess.isnumeric():
            user_guess = input(str(a))
            if not user_guess.isnumeric():
               q.empty_thread().start()
               only = "numbers only please"
               print(red + f'{only:^19}')
        user_guess = int(user_guess)
        if not user_guess == a.ans:
            print(red+ progress_bar(done/how_many))
            q.fail_thread().start()
            ask(a)
    
    print(screen)
    intro = 'press enter'
    _ = input(f'{intro:^19}')
    
    length = len(player.list)

    for _ in range(how_many):
        i = random.randint(0,length-1)
        print(yellow + progress_bar(done/how_many))
        start = time.perf_counter()
        ask(player.list[i])
        finish = time.perf_counter()
        elapsed = finish - start
        Problem.update_avg(player.list[i], elapsed)
        if player.list[i].avg < 5:
            Problem.next_problem(player.biggest)
            player.list[i] = player.biggest
            print('replaced')
            player.mastered += 1
            q.success_thread().start()
        done += 1
    

    d = 'done'
    print(bg_rgb(210,180,110) + rgb(0,0,0) + f'{d:^os.get_terminal_size()}' + clear + green)  
    print(q.frog + '-great job!' '\n' + yellow + 'practice pays off.' + '\n' +cyan +'mastered: ' + str(player.mastered) + ' facts')
    
    _ = input()

if __name__ == '__main__':
    name = input('enter your name\n')
    filename = name + '.dat'
    try:
        with open(filename, 'rb') as storage:
            player = pickle.load(storage)
    except EOFError:
        pass
    except FileNotFoundError:
        choice = input('player not in database,\n make new account?\n')
        if choice[0].lower() == 'y':
            pwd = getpass.getpass('passcode?')
            if pwd == '646169':
                player = Player(name, 7)
    dur = input("how many problems should we do?\n")
    dur = int(dur)
    times(player, dur)
    with open(filename, 'wb') as out:
        pickle.dump(player, out)

