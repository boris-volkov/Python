# CALCULATOR QUEST by BORIS VOLKOV
# This program was made to run in an ubuntu terminal,
# have fun and enjoy! 

import time
import random
import math
import csv
import numpy as np
import os.path
from colors import rgb, bg_rgb
import sys
from os import path
from threading import Thread

mode = False
level = 5
g_elapsed = 0
g_limit = 0

#----------------------------------------------------- Game Strings
margin = '       '
divi        = u'\u2797'
cyan        = '\u001b[96m'
yellow      = rgb(210,180,110)
green       = '\u001b[92m'
red         = '\u001b[91m'
bold        = '\u001b[1m'
clear       = '\u001b[0m'
screen      = '\033[2J'
sword       = '\U0001F5E1'
shield      = '\U0001F6E1'
plus        = u'\u2795'
minus       = u'\u2796'
times       = u'\u274c'
divi        = u'\u2797'
frog        = '\U0001F438'

def intro_string():
    return("    ➕ ➖ ❌ ➗\n" +

            cyan +  ' CALCULATOR  QUEST       ' +sword+ " 🐯" +shield)


#---------------------------------------------------Game Sounds
dur1 = 0.05
dur2 = 0.1

semitone = (16/15)
whole_tone = (9/8)
minor_third = (6/5)
major_third = (5/4)
perfect_fourth = (4/3)
tritone = (7/5)
perfect_fifth = (3/2)
minor_sixth = (8/5)
major_sixth = (5/3)
minor_seventh = (9/5)
major_seventh = (15/8)

freq = 220
def success_sound():
    freq1 = 2*freq 
    freq2 = 2*freq*whole_tone 
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq2))

def name_entered():
    freq1 = freq*(15/16)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(.25,freq1))

def name_thread():
    return Thread(target = name_entered)

def success_thread():
    return Thread(target = success_sound)

def speed_bonus_sound():
    freq1 = 2*freq 
    freq3 = 2*freq*major_third 
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq3))

def speed_thread():
    return Thread(target = speed_bonus_sound)

def fail_sound():
    freq1 = freq * (15/16)
    freq2 = freq * (2/3)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq2))

def fail_thread():
    return Thread(target = fail_sound)

def null_sound():
    dur1 = .1
    freq1 = 564
    os.system('play -nq -t alsa synth {} trapezium {} tremolo 10 40 '.format(dur1,freq1))

def empty_thread():
    return Thread(target = null_sound)

def intro_song():
    durs =      [.5, .5  , .125 , .125 , .125 , .5]
    freqs= freq*np.array([1 ,(15/16),(6/5),(6/5),(2/3),  1])
    bass = freq*np.array([(1/2),(2/3),(3/5),(3/5), (1/2), (1/2) ])
    for i in range(len(freqs)):
        os.system('play -nq -t alsa synth {} sine {} trapezium {}'.format(durs[i], bass[i] ,freqs[i]))

def intro_thread():
    return Thread(target = intro_song)

def finish_song():
    durs =     [.5, 0.25, 0.25, .5] 
    freqs=freq*np.array([1.5 , 1.25, .935,  1])
    for i in range(len(freqs)):
        os.system('play -nq -t alsa synth {} trapezium {}'.format(durs[i],freqs[i]))
    
#-----------------------------------------------------------GAME METHODS:
#a logistic scoring function
def score(x):
    L = 3
    m = 3.8
    k = 1
    v = 0.3
    score = L/(1+math.exp(k*(x-m-math.log(level,10)))) + v
    return score

#to make the output aligned
def make_string(opflag, upper, lower, answer): 

    uLen = len(str(upper))
    lLen = len(str(lower))
    aLen = len(str(answer))
    digits = max(uLen, lLen, aLen-3)

    return(cyan + 
              margin + ' '*3  +  f'{str(upper):>{digits}}'   + '\n' +
              margin + yellow + bold + opflag  + clear + cyan + 
                       ' '*1  +  f'{str(lower):>{digits}}'   + '\n' +
              margin + '-'*(3 + digits)                      + '\n' +
              margin + ' '*(3 + digits - aLen)                       
            )

#does the time computation and re-asking if necessary    
def ask(a,b,c,op):
    global level
    global g_elapsed
    start = time.perf_counter()
    user_guess = ""
    while not user_guess.isnumeric():
        user_guess = input(make_string(op,a,b,c))
        if not user_guess.isnumeric(): 
            print(red + 'numbers only please')
            empty_thread().start()
    user_guess = int(user_guess)    
    finish = time.perf_counter()
    elapsed = finish - start
    g_elapsed += elapsed
    if not user_guess == c:
        print(red + progress_bar(min(1, g_elapsed/g_limit)))
        fail_thread().start()
        if level > 5 :
            level -= 1
    return (user_guess == c, elapsed)

#each operation will keep its own records
class Operation(object):
    count = 0
    weight = 1
    av_time = 0
    mistakes = 0

    def update(self,a, b, c, op):
        global level
        global g_limit
        global g_elapsed
        question_time = 0
        
        x = ask(a,b,c,op)
        correct = x[0]
        first_try = correct
        question_time += x[1]
        while correct == False:
            x = ask(a,b,c,op)
            correct = x[0]
            question_time += x[1]

        self.av_time = (self.av_time*self.count + question_time)
        self.count += 1
        self.av_time = self.av_time/self.count
        success_thread().start() 
        level += score(question_time)
        print(yellow + progress_bar(g_elapsed/g_limit))
        return question_time

#each operation will have its own number choosing method
#and record-keeping 
class Addition(Operation):
    def question(self):
        a = random.randint(round(level - 4),round(level*2))
        b = random.randint(round(level - 4),round(level*2))
        c = a + b
        return self.update(a,b,c,plus)

class Subtraction(Operation):
    def question(self):
        b = random.randint(round(math.log(level,2)),round(level*2))
        c = random.randint(round(math.log(level,2)),round(level*2))
        a = b + c
        return self.update(a,b,c,minus)

class Multiplication(Operation):
    def question(self):
        a = random.randint(round(level/3), round(level*2/3 + 3))
        b = random.randint(3,10 + round(math.log(level, 16)))
        c = a*b
        return self.update(a,b,c,times)

class Division(Operation):
    def question(self):
        a = level*11
        while a >= level*10:
            c = random.randint(math.floor(level/3),math.ceil(level/2))
            b = random.randint(2,math.ceil(level/2))
            a = b*c
        return self.update(a,b,c,divi)

def progress_bar(n):
    bars = ['' , '\U0000258F','\U0000258E','\U0000258D', '\U0000258C', '\U0000258B', '\U0000258A' , '\U00002589', '\U00002588']
    progress = bars[-1]*int(n//(1/19))
    rem = (n/(1/19))-(n//(1/19))
    progress = progress +  bars[int(rem*8//1)]
    return progress


def challenge(limit, lvl = 5,
               addition = True, 
               subtraction = True, 
               multiplication = True, 
               division = True):
    while 1:
        global level
        global g_elapsed
        global g_limit
        g_limit = limit
        g_elapsed = 0
        total_probs = 0
        local_time = time.asctime( time.localtime(time.time()) )
        level = lvl
        print(intro_string())
        adds = Addition()
        subs = Subtraction()
        mult = Multiplication ()
        divs = Division()
        #intro_thread().start()
        age = ''
        while age == '':
            age = input(yellow + '  ENTER your name  \n  ' + green)
            if age == '':
                print('\033[3A')
                fail_thread().start()
        name_thread().start()
        print(screen)
        total_time = 0
        while total_time < limit:
            if addition       : 
                elapsed = adds.question()
                total_time += elapsed
                total_probs += 1
            if total_time > limit: break
            if subtraction    : 
                elapsed = subs.question()
                total_time += elapsed
                total_probs += 1
            if total_time > limit: break
            if multiplication : 
                elapsed = mult.question()
                total_time += elapsed
                total_probs += 1
            if total_time > limit: break
            if division       : 
                elapsed = divs.question()
                total_time += elapsed
                total_probs += 1
        
        d = 'done'
        print(bg_rgb(210,180,110) + rgb(0,0,0) + f'{d:^19}' + clear + green)
        print(frog + '-great job!' '\n' + yellow + 'practice pays off.' + '\n' +cyan +'level: ' +  str(round(level)))
        finish_song() 

        if division == False or addition == False or subtraction == False or multiplication == False:
            return

        already_there = path.exists('records.csv')
        with open('records.csv', mode='a+') as csv_file:
            fieldnames = ['age', 'level', 'problems', 'time','add_av','sub_av','mul_av','div_av', 'date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not already_there:
                writer.writeheader()
            writer.writerow({'age'     : age,
                             'level'   : round(level), 
                             'problems': total_probs,
                             'time'    : limit,
                             'add_av'  : adds.av_time,
                             'sub_av'  : subs.av_time,
                             'mul_av'  : mult.av_time,
                             'div_av'  : divs.av_time,
                             'date'    : local_time
                            })

        total_time = 0
        level = 5
        mode = False
        adds = None
        subs = None
        mult = None
        divs = None
        _ = input()
#if the program is called directly from the terminal

if __name__ == '__main__':
    if len(sys.argv) < 2:
        challenge(60)
    elif len(sys.argv) > 2 and sys.argv[2] == 'as':
        challenge(int(sys.argv[1]),division=False, multiplication=False)
    elif len(sys.argv) > 2 and sys.argv[2] == 'd':
        challenge(int(sys.argv[1]), lvl = 30, addition = False, multiplication=False, subtraction = False)
    else:
        challenge(int(sys.argv[1]))

