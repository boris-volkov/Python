import random, time, os, sys, colors
from itertools import cycle

class Problem:
    ops = { '+': int.__add__,
            '-': int.__sub__,
            '*': int.__mul__,
            '/': int.__floordiv__ }
    
    def __init__(self, a, b, op):
        self.top = a
        self.bot = b
        self.op = op
        self.ans = Problem.ops[op](a, b)
        self.streak = 0 # graduate after a streak
        self.count = 0
    
    def __iadd__(self, n): # this is probably a stupid choice
        self.count += n
        self.streak = 0 if n == 0 else self.streak + 1
        if self.streak > 1:
            new = 
        return self
    
    @staticmethod
    def progress_bar(n): # should this be internal to play() ? 
        w = os.get_terminal_size()[0]
        bars = ['', '\u258F', '\u258E', '\u258D', '\u258C', 
                    '\u258B', '\u258A', '\u2589', '\u2588']
        progress = bars[-1]*int(n//(1/w))
        rem = (n/(1/w))-(n//(1/w))
        progress = progress + bars[int(rem*8//1)]
        return progress

    def __str__(self): # can this kind of function have an input n?
        w, h = os.get_terminal_size()
        return '%d%s%d=' % (self.top, self.op, self.bot)

    def __repr__(self):
        return '%d%s%d=%d'%(self.top, self.op, self.bot, self.ans)

    def ask(self, n):
        try:
            answer = int(input(str(self)))
        except ValueError:
            self.ask(n+1)
        if answer == self.ans:
            self += 1
            return n
        else:
            self += 0
            return self.ask(n+1)
    
    def __next__(self, biggest):
        if self.top > self.bot:
            return Problem(biggest.top, biggest.top + 1, biggest.op)
        else:
            return Problem(biggest.top + 1, 0, biggest.op)

    def copy(self):
        copy = Problem(self.top, self.bot, self.op)

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.answered = 0
        self.deck =  { '+' : [next(self.gens['+']) for _ in range(30)],  
                       '-' : [next(self.gens['-']) for _ in range(30)],
                       '*' : [next(self.gens['*']) for _ in range(30)],
                       '/' : [next(self.gens['/']) for _ in range(30)] }
        self.biggest =  { '+' : self.deck['+'][-1], 
                          '-' : self.deck['-'][-1],
                          '*' : self.deck['*'][-1],
                          '/' : self.deck['/'][-1] }
        self.graveyard = []  # "dead" cards, to add to records at the end. 

    def play(self, n):
        ops = '+-*/'
        opstring = input('which operations?')
        if opstring == 'all':  opstring = '+-*/'
        else: opstring = ''.join(op for op in ops if op in opstring) 
        print(opstring)
        i = n
        for op in cycle(opstring):
            prob = random.choice(self.deck[op])
            prob.count += prob.ask(1)
            i -= 1
            if i == 0: break


if __name__ == '__main__':
    import shelve 
    db = shelve.open('players')

    name = input('name?')
    if name in db:
        P = db[name]
    else:
        age = input('age?')
        P = Player(name, age)

    n = input('how many problems should we do?')
    try:
        P.play(n)
    except (KeyboardInterrupt, EOFError):
        print('thanks for playing!')
    finally:
        db[name] = P
        db.close()
