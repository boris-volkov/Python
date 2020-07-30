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
import csv
import os.path
import sys
from os import path
import speech_recognition as sr
import pocketsphinx as spx

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source, duration = 3)

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current



level = 5
total_time = 0
margin = '   '
mode = False

#strings -----------------------------------------------------
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

#-----------------------------------------------------------------------
#GAME METHODS:
#a logistic scoring function
def score(x):
    L = 3
    m = 3.8
    k = 1
    v = 0.3
    score = L/(1+math.exp(k+(x-m))) + v
    return score

#to make the output aligned
def make_string(upper, lower, answer, opflag): 

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
    global total_time
    global level
    global mic
    mistake_flag = False
    start = time.perf_counter()
    print(make_string(a,b,c,op), end = '')
    user_guess = ""
    while not isinstance(user_guess, int):
        try:
            with mic as source:
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1.5)
                user_said = r.recognize_sphinx(audio)
                user_guess = text2int(user_said)
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
    print(user_guess)	        
    finish = time.perf_counter()
    elapsed = finish - start
    total_time += elapsed
    if not user_guess == c: 
        print(mistake + red + '\n                                            -1')
        mistake_flag = True
        if level > 5 :
            level -= 1
    return (user_guess == c, elapsed, mistake_flag)

#each operation will keep its own records
class Operation(object):
    count = 0
    weight = 1
    av_time = 0
    mistakes = 0

    def update(self,a, b, c, op):
        global level
        correct = False
        while correct == False:
            x = ask(a,b,c,op)
            correct = x[0]
        self.av_time = (self.av_time*self.count + x[1])
        self.count += 1
        self.av_time = self.av_time/self.count
        if x[1] < 2 + math.log(level,10) and not x[2]:
            print(speed_bonus)
        else:
            print(success)    
        level += score(x[1])
        print(level_str())
        return x[1]

#each operation will have its own number choosing method
#and record-keeping 
class Addition(Operation):
    def question(self):
        a = random.randint(round(level - 4),round(level+20))
        b = random.randint(round(level - 4),round(level+20))
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
        a = random.randint(round(level - 3), round(level + 3))
        b = random.randint(3,10 + round(math.log(level, 7)))
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

def challenge(limit, hardmode = False, lvl = 10,
               addition = True, 
               subtraction = True, 
               multiplication = True, 
               division = True):
    global total_time
    global mode
    global level
    level = lvl
    mode = hardmode
    print(intro_string())
    adds = Addition()
    subs = Subtraction()
    mult = Multiplication ()
    divs = Division()
    age = input(yellow + '    Are you prepared? ENTER your tag to begin\n                      ')
    while total_time < limit:
        if addition       : total_time += adds.question()
        if subtraction    : total_time += subs.question()
        if multiplication : total_time += mult.question()
        if division       : total_time += divs.question()
    print("  " + frog + " Great job!")
    total_probs = adds.count + subs.count + mult.count + divs.count

    print("     You got to level "+yellow+ str(round(level)) + cyan + 
          " in "+yellow+str(limit)+cyan+" seconds\n")
    print(yellow+" High five! " + hand + "  You get better every time!\n\n\n")
    
    already_there = path.exists('records_voice.csv')
    with open('records_voice.csv', mode='a+') as csv_file:
        fieldnames = ['age', 'level', 'problems', 'time','add_av','sub_av','mul_av','div_av']
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
                         'div_av'  : divs.av_time
                        })

    total_time = 0
    level = 5
    mode = False
    adds = None
    subs = None
    mult = None
    divs = None


#challenge(10)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        challenge(180)
    elif len(sys.argv) > 2 and sys.argv[2] == 'as':
        challenge(int(sys.argv[1]),division=False, multiplication=False)
    else:
        challenge(int(sys.argv[1]))

