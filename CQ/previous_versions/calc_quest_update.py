import time
import random
import math

level = 5
total_time = 0
margin = '  '

blue = '\u001b[96m'
clear = '\u001b[0m'

success     = '                      \U0001F538' 
mistake     = '                      \U0001f62d'
no_num      = '                      \U00012049'
speed_bonus = '                      \U0001272B'
sword       = '\U0001F5E1'
shield      = '\U0001F6E1'
frog        = '\U0001F438'
hand        = '\U0001F590'
castle      = '\U0001F3EF'
fire        = '\U0001F525'
minus       = '\U00012796'

#a logistic scoring function
def score(x):
    L = 3
    m = 3.8
    k = 1
    v = 0.3
    score = L/(1+math.exp(k+(x-m))) + v
    return score

#to make the output aligned
def make_string(opflag, upper, lower, answer): 
    opS = "?"                   
    if opflag == 'add':
        opS = "+"
    elif opflag == 'subtract': 
        opS = "-"
    elif opflag == 'multiply':
        opS = "x"
    elif opflag == 'divide':
        opS = "÷"
    uLen = len(str(upper))
    lLen = len(str(lower))
    aLen = len(str(answer))
    digits = max(uLen, lLen, aLen-3)
    return  ( blue +
              margin +        ' '*2  +  f'{str(upper):>{digits}}'   + '\n' +
              margin +  opS + ' '*1  +  f'{str(lower):>{digits}}'   + '\n' +
              margin +        '-'*(2 + digits)                      + '\n' +
              margin +        ' '*(2 + digits - aLen)                       
            )

#does the time computation and re-asking if necessary    
def ask(a,b,c,op):
    global total_time
    start = time.perf_counter()
    user_guess = int(input(make_string(op,a,b,c)))
    finish = time.perf_counter()
    elapsed = finish - start
    total_time += elapsed
    if not user_guess == c: print(mistake) 
    return (user_guess == c, elapsed)

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
        self.count += 1
        if x[1] < 2:
            print(speed_bonus)
        else:
            print(success)
        print(x[0])
        print(x[1])
        print(score(x[1]))
        level += score(x[1])
        return x[1]


#each operation has its own number choosing rules 
class Addition(Operation):
    def question(self):
        a = random.randint(1,round(level))
        b = random.randint(1,round(level))
        c = a + b
        return self.update(a,b,c,'add')

def challenge(limit):
    global total_time
    adds = Addition()
    while total_time < limit:
        total_time += adds.question()

    print("you did  " + str(adds.count) + " problems")
    print(level)


challenge(20)
