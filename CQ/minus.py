import random
import time
import quest as q
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
    upper = a[0]
    lower = a[1]
    answer= a[2]

    uLen = len(str(upper))
    lLen = len(str(lower))
    aLen = len(str(answer))
    digits = max(uLen, lLen, aLen-3)

    return(cyan +
              margin + ' '*2  +  f'{str(upper):>{digits}}'   + '\n' +
              margin +
                    yellow + bold + '-'  + clear + cyan +
                       ' '*1  +  f'{str(lower):>{digits}}'   + '\n' +
              margin + '-'*(2 + digits)                      + '\n' +
              margin + ' '*(2 + digits - aLen)
            )


def progress_bar(n):
    bars = ['' , '\U0000258F','\U0000258E','\U0000258D', '\U0000258C', '\U0000258B', '\U0000258A' , '\U00002589', '\U00002588']
    progress = bars[-1]*int(n//(1/19))
    rem = (n/(1/19))-(n//(1/19))
    progress = progress +  bars[int(rem*8//1)]
    return progress

def times(limit):
    done = 0
    table = []
    for i in range(2,limit):
        for j in range(i,limit):
            table.append((j,i,j-i))
    random.shuffle(table)

    full_list = len(table)

    def ask(a):
        user_guess = ""
        while not user_guess.isnumeric():
            user_guess = input(make_string(a))
            if not user_guess.isnumeric():
               q.empty_thread().start()
               only = "numbers only please"
               print(red + f'{only:^19}')
        user_guess = int(user_guess)
        if not user_guess == a[2]:
            print(red+ progress_bar(done/full_list))
            q.fail_thread().start()
            ask(a)
    print(screen)
    intro = 'press enter'
    _ = input(f'{intro:^19}')
    start = time.perf_counter()
    while table:
        print(yellow + progress_bar(done/full_list))
        ask(table.pop())
        q.success_thread().start()
        done += 1
    finish = time.perf_counter()
    elapsed = round(finish - start)
    d = 'done'
    print(bg_rgb(210,180,110) + rgb(0,0,0) + f'{d:^19}' + clear + green)  
    print(q.frog + '-great job!' '\n' + yellow + 'practice pays off.' + '\n' +cyan +'took: ' +  str(elapsed) + " seconds")
    _ = input()

if __name__ == '__main__':
    times(int(sys.argv[1]) + 1)
