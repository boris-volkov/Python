import random
import time
import sys

def make_string(a):
    margin = '       '
    upper = a[0]
    lower = a[1]
    answer= a[2]

    uLen = len(str(upper))
    lLen = len(str(lower))
    aLen = len(str(answer))
    digits = max(uLen, lLen, aLen-2)

    return(   margin + ' '*2 + f'{str(upper):>{digits}}' + '\n' +
              margin + 'x' + ' '*1 + f'{str(lower):>{digits}}' + '\n' +
              margin + '-'*(2 + digits)  + '\n' +  margin +
              ' '*(2 + digits - aLen) )

def times(limit):
    done = 0
    table = []
    for i in range(2,limit):
        for j in range(i,limit):
            table.append((j,i,i*j))
    random.shuffle(table)
    total_problems = len(table)
    done = 0
    def ask(a):
        user_guess = ""
        while not user_guess.isnumeric():
            user_guess = input(make_string(a))
            if not user_guess.isnumeric():
               only = "numbers only please"
        user_guess = int(user_guess)
        if not user_guess == a[2]:
            ask(a)
    print('\n')
    intro = 'press enter'
    _ = input(f'{intro:^19}')
    start = time.perf_counter()
    while table:
        ask(table.pop())
        done += 1
    finish = time.perf_counter()
    elapsed = round(finish - start)
    print('-great job!' '\n' + 'practice pays off.' +
            '\n' +'took: ' +  str(elapsed) + " seconds")
    _ = input()

if __name__ == '__main__':
    times(int(sys.argv[1]) + 1)
