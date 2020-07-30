import colors
import time
from random import randint, random
from threading import Thread
import os

runtime = 0

dur1 = 0.05
dur2 = 0.1

def yes():
    freq1 = 440
    freq3 = 440*(5/4)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq3))

def yes_thread():
    return Thread(target = yes)

def no():
    freq1 = 440 * (15/16)
    freq2 = 440 * (2/3)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq2))

def no_thread():
    return Thread(target = no)

def track_time(func):
    def inner(*args, **kwargs):
        global runtime
        begin = time.time()
        correct = func(*args, **kwargs)
        end = time.time()
        runtime += (end - begin)
        return correct
    return inner

@track_time
def ask(level):
    a = randint(level//2, level)
    print()
    while 1:
        if level < 30:
            print(colors.cyan + '   √'+ colors.yellow +  str(a**2) + colors.green)
        else:
            print(colors.cyan + '   ∛'+ colors.yellow +  str(a**3) + colors.green)
        answer = input('    ')
        if str(a) in answer:
            yes_thread().start()
            return 1
        no_thread().start()

def quest(t):
    problem_count = 0
    i = 5
    while runtime < t:
        problem_count += 1
        ask(i)
        i += 3
    return problem_count

print(colors.hide_cursor)
print(colors.green + "   √" + colors.cyan + "QUEST")
print(colors.yellow + " press enter")
_ = input()
count = quest(300)
print(colors.yellow + "wow! \n you solved:")
print(colors.green + str(count)+colors.yellow+ ' roots', end = '\r')
_ = input()
