import colors
from random import randint
import time
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
        func(*args, **kwargs)
        end = time.time()
        runtime += (end - begin)
    return inner

@track_time
def ask(lev): 
    a = 0
    b = 0
    while a == 0:
        a = randint(-lev,lev)
    while b == 0:
        b = randint(-lev,lev)

    while 1:
        print(colors.cyan + 'a·b = '+ colors.yellow +  str(a*b))
        print(colors.green + 'a+b = '+ colors.yellow +  str(a+b))
        answer = input()
        if str(a) in answer and str(b) in answer:
            yes_thread().start()
            return
        no_thread().start()

def quest(dur):
    problem_count = 0
    i = 5
    while runtime < dur:
        ask(i)
        i += 2
        problem_count += 1
    return problem_count

print(colors.cyan + "FACTOR QUEST")
print(colors.yellow + "press enter")
_ = input()
count = quest(300)
print(colors.clear_screen + colors.green + str(count) + colors.yellow + ' answered')
_ = input()
