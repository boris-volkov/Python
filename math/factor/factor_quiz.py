import random
from record_keeping import *
from constants import *
from colors import *

def factors(x):
    factors = [i for i in range(1,x//2 + 1) if x%i == 0]
    factors.append(x)
    return factors

binomial = '(%dx + %d)•(%dx + %d)'
neg_bino = '-(%dx + %d)•(%dx + %d)'
trinomial = '%dx² + %dx + %d'

def subtraction(S): # this is to clear away '+ -' pattern and replace with '-'
    while '+ -' in S:
        L = list(S)
        L[S.index('+ -'):S.index('+ -')+3] = '- '
        S = ''.join(L)
    return S

def solves(x, *tup): # check if a factorization is correct
    if x[0]*x[-2] == tup[0]*tup[-2]:
        if x[1]*x[-1] == tup[1]*tup[-1]:
            if x[0]*x[-1]+x[1]*x[-2] == tup[0]*tup[-1]+tup[1]*tup[-2]:
                return 1
    return 0

def wrong_answer(a,b,c,d,length): # meant to produce wrong answers that look right
        f = factors(abs(a*c))	  
        l = factors(abs(b*d))
        if len(l) == 1:
            l.append(2)
        answers = []
        while len(answers) < length:
            f_choice = random.choice(f)
            l_choice = random.choice(l)
            l_choice *= random.choice([1,-1])
            x = (f_choice, l_choice, (a*c)//f_choice, (b*d)//l_choice)
            if solves(x,a,b,c,d):
                continue
            else: answers.append(x)
        return answers

def cleaned(x): # makes a cleaner replacement of the polynomial strings. should probably be a class
    return x.replace(' 1x',' x').replace('+ 0x +', '+').replace('+ 0x -', '-').replace('(1x', '(x').replace('1x²', 'x²')

def ask_question(a=0,b=0,c=0,d=0):
    global streak
    if a == 0:
        a = random.randint(1,(streak + 3)//2)
        def pick_coeff(a,b, other = 1): # picks good coefficients
            c = 0
            while c == 0 or len(set(factors(abs(c))).intersection(set(factors(abs(other))))) >= 2:
                c = random.randint(a,b)
            return c
        b = pick_coeff(-(streak + 10)//2,(streak + 10)//2, a)
        c = pick_coeff(-(streak +10)//3,(streak + 10)//3)
        d = pick_coeff(-(streak + 10)//2,(streak + 10)//2, c)

    tri = trinomial % (a*c, b*c + a*d, b*d)
    bi = binomial % (a,b,c,d)
    nonegstri = subtraction(tri)
    nonegsbi = subtraction(bi)
    print(yellow + '\x1b[1m', 'Factor  : ', cleaned(nonegstri), '\x1b[0m')

    choices = wrong_answer(a,b,c,d,7)
    choices = list(set(choices))
    correct = random.randint(0,len(choices) -1)
    choices[correct] = (a,b,c,d)
    def negated(tup):
        new_tup = (tup[0], tup[1], -tup[2], -tup[3])
        return new_tup

    print(yellow)
    for i in range(len(choices)):
        if choices[i][2] < 0:
            choices[i] = subtraction(neg_bino % negated(choices[i]))
        else:
            choices[i] = subtraction(binomial % choices[i])
        print(' '*4, base_nums[i] + '  ' , cleaned(choices[i])) 
    print('\n'*(6-len(choices)), end = '')
            
    guess = input('\nWhich is correct?   ')
    print('\x1bc')
    if guess == str(correct+1):
        print(cyan + 'wow, you\'re right!')
        streak += 1
        #percent = streak/WINCOND*100
        print(cleaned(nonegstri), '=\n', cleaned(choices[correct]))
        print(green + '█'*streak + '░'*(WINCOND-streak) + ' ' + str(streak))
        print()
    else:
        print(cyan + '\ntry again...\nI know you can do it!')
        streak = max(0, streak - 1)
        #percent = streak/WINCOND*100
        print(yellow + '▓'*streak + '░'*(WINCOND-streak) + ' ' + red + str(streak))
        print()
        ask_question(a,b,c,d)

if __name__ == '__main__':
    import time
    import pickle
    import sys
    
    if len(sys.argv) > 1:
        WINCOND = int(sys.argv[-1])

    print('\x1bc')
    streak = 0
    start = time.time()
    date = time.ctime()
    print(cyan + '\x1b[1m     • FACTORING CHALLENGE •\x1b[0m')
    print(red + faint +  'ENTER the number of your choice')
    print('Answering correctly gains a point')
    print('But incorrect guesses lose a point')
    print('Can you get to 20?' + reset)
    while streak < WINCOND:
        ask_question()

    record_name = str(WINCOND) + '_record.dat'
    elapsed = time.time() - start
    finish = time.ctime()
	
    try:
        with open(record_name, 'rb') as records:
            board = pickle.load(records)
    except FileNotFoundError:
        board = top_ten()
    
    
    print('\x1bc\n\n')
    if board.needed(elapsed):
        print('Excellent time!\nYou\'re in the top 10!\nEnter your name!')
        name = input()
        entry = record(name, elapsed)
        board.insert(entry)

        #print('\x1bc\n\n')
        #print('\n' * 5 )
        print('current round started\n', date)
        print('top 10 times for %d points:' % WINCOND)
        print(board)

    else:
        print('current round started:\n', date)
        print('finished:\n', finish)
        print('took', f'{elapsed:.2f}', 'seconds')
        print('wow, great job!')

    with open(record_name, 'wb') as rec:
        pickle.dump(board, rec)
	
