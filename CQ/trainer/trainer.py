import random, os, getpass, pickle, time, sys
import effects as q
from colors import rgb, bg_rgb, hide_cursor


margin      = '       '
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
    def __init__(self, a, b):
        self.top = a
        self.bot = b
        self.ans = None # to be set by particular operations
        self.avg = 0
        self.count = 0

    def __eq__(self, other):
        if self.top == other.top:
            return self.bot == self.bot

    def update_avg(self, time):
        if self.avg !=0:
            self.avg = (self.avg*2 + time)/3
        else:
            self.avg = time
    
    def next_problem(self):
        if self.top > self.bot:
            self.bot += 1
        else:
            self.top += 1
            self.bot = 2
        self.ans = self.top*self.bot
        self.avg = 0
        self.count = 0
    
    def __str__(self):
        return '{}x{}={} | attempts: {} | average time: {}'.format(self.top, self.bot, 
                                                        self.ans, self.count, self.avg )
    def copy(self):
        return Problem(self.top, self.bot)

class Times(Problem): # Need to independently test if this works
    def __init__(self, a, b):
        me = Problem(a, b)
        me.ans = a*b
        return me

def generate_probs(limit):
    table = []
    for i in range(2,limit):
        for j in range(2,i+1):
            table.append(Problem(j,i))
    return table

class Player(object):
    def __init__(self,name, limit):
        self.name = name
        self.list = generate_probs(limit)
        self.biggest = Problem(limit-1, limit-1) 
        self.mastered = 0
    def __iter__(self):
        return iter(self.list)
    def __setitem__(self, index, value):
        self.list[index] = value
    def __getitem__(self, index):
        return self.list[index]
    def __repr__(self):
        for i in self.list:
            print(self[i])
            time.sleep(0.1)

def progress_bar(n):
    bars = ['' , '\U0000258F','\U0000258E','\U0000258D', 
            '\U0000258C', '\U0000258B', '\U0000258A' , 
            '\U00002589', '\U00002588']
    progress = bars[-1]*int(n//(1/19)) # my screen is 19 chars across
    rem = (n/(1/19))-(n//(1/19))
    progress = progress +  bars[int(rem*8//1)]
    return progress


# main loop function


def times(player, current_record, how_many):
    done = 0

    def ask(a): # perhaps make this an internal method of class Problem
        user_guess = ""
        while not user_guess.isnumeric():
            user_guess = input(make_string(a))
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
        ask(player.list[i]) # do I really need to be indexing the list all the time?
        finish = time.perf_counter()
        elapsed = finish - start
        Problem.update_avg(player.list[i], elapsed)
        player.list[i].count += 1 
        if player[i].avg < 4:
            Record.update(current_record, player.list[i])
            Problem.next_problem(player.biggest)        # update biggest problem
            player[i] = Problem.copy(player.biggest)    
            player.mastered += 1
            q.success_thread().start()
        done += 1
    

    d = 'done' # for formatting
    print(bg_rgb(210,180,110) + rgb(0,0,0) + f'{d:^19}' + clear + green)  
    print(q.frog + '-great job!' '\n' + yellow + 
            'practice pays off.' + '\n' + cyan + 'mastered: ' + 
            str(player.mastered) + ' facts')
    _ = input()


#*******************Record Keeping******************************

class Record_Problem(object):
    def __init__(self, a, b):
        self.top = a
        self.bot = b
        self.players = 0
        self.av_attempts = 0

    def __eq__(self, other):
        if self.top == other.top:
            return self.bot == other.bot
 
    def __str__(self):
        return '{}x{}, average attempts: {}'.format(self.top, self.bot,
                                                    self.av_attempts)

class Record(object):
    def __init__(self):
        self.list = []
    
    def __iter__(self):
        return iter(self.list)

    def update(self, prob):
        for p in self.list:
            if p == prob:
                p.av_attempts = (p.av_attempts*p.players + prob.count)/(p.players + 1)
                p.players += 1
                return 
        new_entry = Record_Problem(prob.top, prob.bot)
        new_entry.av_attempts = prob.count
        self.list.append(new_entry)                
    def __repr__(self):
        for i in self:
            print(i)
            time.sleep(1)



if __name__ == '__main__':
    name = input('enter your name\n'+green)
    filename = name + '.dat'
    
    # unpack player and record objects from file
    try:
        with open('records.dat', 'rb') as records:
            current_record = pickle.load(records)
    except FileNotFoundError:
        current_record = Record()
    try:
        with open(filename, 'rb') as storage:
            player = pickle.load(storage)
    except EOFError:
        pass
    except FileNotFoundError:
        choice = input(yellow + 'player not in database,\n make new account?\n'+ green)
        if choice[0].lower() == 'y':
            pwd = getpass.getpass(yellow + 'passcode?')
            if pwd == '646169':
                player = Player(name, 9)
    
    #decide how many problems to do and do them
    dur = input(yellow + "how many problems\n should we do?\n" + green)
    dur = int(dur)
    times(player, current_record, dur)
    """ 
    # for debugging
    for i in current_record:
        print(i)
    print('player.biggest = ' +str(player.biggest))
    for i in player:
        print(i)
    """
    # save player and record
    with open(filename, 'wb') as out:
        pickle.dump(player, out)
    with open('records.dat', 'wb') as rec:
        pickle.dump(current_record, rec)
