# CALCULATOR QUEST by BORIS VOLKOV
# This program was made to run in an ubuntu terminal,
# so some spacing adjustments may need to be made in the
# make_string() method to make it look good on other systems
# to run the game, import calculator_quest in a python terminal
# and run calculator_quest.challenge(n), where n is the 
# number of seconds you want to play.
# have fun and enjoy! 

import time
import random
import math
import numpy as np
import csv
import os.path
import sys
from os import path
from threading import Thread
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
plt.rcParams['axes.facecolor'] = '#772953'

mode = False
level = 5
bonus_count = 0
correct_count = 0
skull_count = 0

#----------------------------------------------------- Game Strings
margin = '   '
success     = '                       \U0001F538' 
crying      = '                       \U0001f62d'
no_num      = '                       \U00012049'
speed_bonus = '                       '+ u"\u2728"
crab        = '                       \U0001F980' 
sword       = '\U0001F5E1'
shield      = '\U0001F6E1'
mistake     = '                       \U0001F480'
frog        = '\U0001F438'
hand        = '\U0001F590'
castle      = '\U0001F3EF'
fire        = '\U0001F525'
bunny       = '                       \U0001F430'
plus        = u'\u2795'
minus       = u'\u2796'
times       = u'\u274c'
divi        = u'\u2797'
cyan        = '\u001b[96m'
yellow      = '\u001b[93m'
green       = '\u001b[92m'
red         = '\u001b[91m'
bold        = '\u001b[1m'
clear       = '\u001b[0m'
screen      = '\033[2J'
monsters = ['                       \U0001F980',
            '                       \U0001F988',
            '                       \U0001F421',
            '                       \U0001F987',
            '                       \U0001F40A',
            '                       \U0001F991',
            '                       \U0001F329']

def error():
    i = random.randint(0,len(monsters)-1)
    return monsters[i]

def intro_string():
    return(screen+green+minus*25 + 
"\n 🏰   🔥   🏰"+bold+"   CALCULATOR QUEST "+clear+green+"   🏰   🔥   🏰\n" +
"             ➕     ➖     ❌     ➗\n" +
" All the calculators in the kingdom have exploded!\n" +
"      Roaming math problems haunt the land...\n" +
"    It is your Quest to save us with your MIND\n\n" +
"         Stay sharp  " +sword+ " 🐯" +shield+"   Have no fear\n" +
minus*25+ '\n' + cyan
)

def level_str():
    return ' '*38 + 'level: '+ yellow + str(round(level)) + cyan + '\n'

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

def freq(x): return 220
def noise(x):
    if x == 1:
        return np.random.normal(0,0.5)
    return np.random.normal(0,3,x)
def success_sound():
    freq1 = 2*freq(level) + noise(1)
    freq2 = 2*freq(level)*whole_tone + noise(1)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq2))

def name_entered():
    freq1 = freq(level)*(15/16)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(.25,freq1))

def name_thread():
    return Thread(target = name_entered)

def success_thread():
    return Thread(target = success_sound)

def speed_bonus_sound():
    freq1 = 2*freq(level) + noise(1)
    freq3 = 2*freq(level)*major_third + noise(1)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq3))

def speed_thread():
    return Thread(target = speed_bonus_sound)

def fail_sound():
    freq1 = freq(level) * (15/16)+ noise(1)
    freq2 = freq(level) * (2/3)+ noise(1)
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
    freqs= freq(level)*np.array([1 ,(15/16),(6/5),(6/5),(2/3),  1])
    bass = freq(level)*np.array([(1/2),(2/3),(3/5),(3/5), (1/2), (1/2) ]) + noise(len(durs))
    for i in range(len(freqs)):
        os.system('play -nq -t alsa synth {} sine {} trapezium {}'.format(durs[i], bass[i] ,freqs[i]))

def intro_thread():
    return Thread(target = intro_song)

def finish_song():
    durs =     [.5, 0.25, 0.25, .5] 
    freqs=freq(level)*np.array([1.5 , 1.25, .935,  1])
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

    return( '\n' + cyan + 
              margin + ' '*3  +  f'{str(upper):>{digits}}'   + '\n' +
              margin +
                    yellow + bold + opflag  + clear + cyan + 
                       ' '*1  +  f'{str(lower):>{digits}}'   + '\n' +
              margin + '-'*(3 + digits)                      + '\n' +
              margin + ' '*(3 + digits - aLen)                       
            )

#does the time computation and re-asking if necessary    
def ask(a,b,c,op):
    global level
    global skull_count
    start = time.perf_counter()
    user_guess = ""
    while not user_guess.isnumeric():
        user_guess = input(make_string(op,a,b,c))
        if not user_guess.isnumeric(): 
            print(bunny +green+'\n                                            ???')
            empty_thread().start()
    user_guess = int(user_guess)    
    finish = time.perf_counter()
    elapsed = finish - start
    #print(elapsed)
    if not user_guess == c:
        skull_count += 1
        print(mistake + red + '\n                                            -1')
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
        global correct_count
        global bonus_count
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
        if question_time < 1 + math.log(level,10) and first_try:
            print(speed_bonus)
            bonus_count +=1
            speed_thread().start()
        else:
            print(success)
            correct_count += 1
            success_thread().start() 
        level += score(question_time)
        print(level_str())
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

def challenge(limit, hardmode = False, lvl = 5,
               addition = True, 
               subtraction = True, 
               multiplication = True, 
               division = True):
    global mode
    global level
    global correct_count
    global bonus_count
    global skull_count
    time_series = [(0,5,'yellow')]
    local_time = time.asctime( time.localtime(time.time()) )
    level = lvl
    mode = hardmode
    print(intro_string())
    adds = Addition()
    subs = Subtraction()
    mult = Multiplication ()
    divs = Division()
    intro_thread().start()
    age = ''
    while age == '':
        age = input(yellow + '    Are you prepared? ENTER your name to begin\n                      ' + green)
        if age == '':
            print('\033[3A')
            fail_thread().start()
    name_thread().start()

    total_time = 0
    while total_time < limit:
        if addition       : 
            total_time += adds.question()
            time_series.append((total_time, level, 'cyan'))
        if total_time > limit: break
        if subtraction    : 
            total_time += subs.question()
            time_series.append((total_time, level, 'red'))
        if total_time > limit: break
        if multiplication : 
            total_time += mult.question()
            time_series.append((total_time, level, 'green'))
        if total_time > limit: break
        if division       : 
            total_time += divs.question()
            time_series.append((total_time, level, 'yellow'))
    
    print("  " + frog + " Great job!")
    total_probs = adds.count + subs.count + mult.count + divs.count
    print("     You got to level "+yellow+ str(round(level)) + cyan + 
          " in "+yellow+str(limit)+cyan+" seconds\n")
    print('    \U0001F538 : ' + yellow + str(correct_count) + cyan + 
          '       ' +  u"\u2728" + ' : ' + yellow + str(bonus_count) + cyan + 
          '       \U0001F480 : ' + red +  str(skull_count) + '\n\n')
    print(cyan+" High five! " + hand + "  You get better every time!\n\n\n")
    finish_song() 

    if division == False or addition == False or subtraction == False or multiplication == False:
        return

    _ = input(yellow + '   press ENTER to see your time chart')
    time_series[-1] = (time_series[-1][0], time_series[-1][1], 'black')
    series_time = [x[0] for x in time_series]
    series_levels = [x[1] for x in time_series]
    colors = [x[2] for x in time_series]
    plt.figure(figsize=(11,8))
    plt.suptitle("your game just now")
    plt.scatter(series_time, series_levels, c=colors)
    plt.xlabel('time (seconds)')
    plt.ylabel('level')
    plt.show()
    
    
    already_there = path.exists('records.csv')
    with open('records.csv', mode='a+') as csv_file:
        fieldnames = ['age', 'level', 'problems', 'time','add_av','sub_av','mul_av','div_av', 'date', 'time_series']
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
                         'date'    : local_time,
                         'time_series' :time_series
                        })

    total_time = 0
    level = 5
    mode = False
    adds = None
    subs = None
    mult = None
    divs = None

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

