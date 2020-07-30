from colors import *
import random, math
from fractions import Fraction
import time


def is_square(apositiveint):
  if apositiveint % 1 != 0 or apositiveint < 0:
    return False
  x = apositiveint // 2
  if x == 0:
      return False
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


class Log(object):
    def __init__(self, base, res, exp, blanked):
        self.base = base
        self.res = res
        self.exp = exp
        self.blanked = blanked

    def __getitem__(self, index):
        return [self.base, self.res, self.exp][index]

    @staticmethod
    def generate_random(level, blanked):
        a = random.choice([2,3,4,5,6])
        if a == 2:
            b = random.randint(-13,13)
        else:
            b = random.randint(-5,5)
        if b > 0 and a**b:
            if random.randint(0,1):
                if (is_square(a**b)):
                    b = Fraction(b,2)
        if b < 0 and a:
            c = Fraction(1, int(a**-b))
        else:
            c = 0 if a == 0 else Fraction(a**b)
        return Log(a,c,b, blanked)

    def __str__(self):
        items = ['log']
        bases = ['\u2080','\u2081','\u2082',
                '\u2083','\u2084','\u2085',
                '\u2086','\u2087','\u2088','\u2089']
        items.append(magenta)
        if self.blanked == 0:
            items.append('\u2093')
        else:
            items.append(bases[self.base]) 
        items.append(reset + '('+ yellow)
        if self.blanked == 1:
            items.append('x')
        else:
            items.append(str(self.res))
        items.append(reset + ')=' + cyan)
        if self.blanked == 2:
            items.append('x')
        else:
            items.append(str(self.exp))

        items.append(reset)
        return ''.join(items)


    def x_out(self, var):
        pass
        
    def wrong(self): # returns (list, answer) tuple
        
        [Log.wrong_exponent, 
         Log.wrong_base, 
         Log.wrong_result,]

    @staticmethod
    def wrong_exponent():
        pass

    def wrong_base():
        pass

    def wrong_result():
        pass


def tip():
    string = green + '☝ ' + reset + 'log' + magenta + '\u2090' + reset + '(' + yellow + 'b' + reset + ')=' + cyan + 'n' + green + ' ⇔ ' + magenta + 'a' + cyan + '\u207F' + reset + '=' + yellow + 'b' + reset
    return string

def play_game(wincond):
    streak = 0
    while streak < wincond:
        print('\x1bc')
        print()
        print(green + '█'*streak + '░'*(wincond-streak) + reset) 
        print()
        unk = random.choice([0,1,2])
        test = Log.generate_random(6,unk)
        if test.exp == 0:
            unk = random.choice([1,2])
            test.blanked = unk
        
        colors = [magenta, yellow, cyan]
        answer = 999
        while 1:
            print(test)
            answer = input(colors[unk] + 'x = ')
            try:
                if Fraction(answer) == Fraction(test[unk]):
                    break
            except ValueError:
                print('\x1bc\n')
                print(rand_f() + '▓'*streak + '░'*(wincond-streak))               
                print(red + 'input malfunction' + reset)
                continue
            except ZeroDivisionError:
                print('\x1bc\n')
                print(cyan + '▓'*streak + '░'*(wincond-streak))                
                print(red + 'what are you trying to do?!', reset)
                continue
            streak = max(0, streak - 1)
            print('\x1bc')
            print(tip())
            print(yellow + '▓'*streak + '░'*(wincond-streak) + ' ' + red+ reset)
            print()
        streak += 1

if __name__ == '__main__':
    wincond = 38
    start = time.time()
    play_game(wincond)
    finish = time.time() - start
    print('\x1bc')
    print()
    print(green + '█'*wincond)

    print(yellow + 'great job!\nyou finished in\n %d seconds' % finish)
    print('it is now\n', red +  time.ctime())
