#FINAL PROJECT!!!
#---------------------------------------------------
import random
import time

number1 = 0
number2 = 0
number3 = 0
class Math(object):
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.score = 0
    def Start(self):
        print('You will face 5 Addition, 5 Subtraction,  5 Multiplication problems, 5 Division problems, & 40 Algebra problems that are Addition, Subtraction, Multiplication, & Division. Up your score by getting the questions correct! Good luck!')
        print('---------------------------------------')
        ready = input('Are you ready?:')
        if ready in ('yes', 'yes!', 'yas', 'yersh', 'yup', 'ye'):
            for i in range(5):
                #Addition
                number1 = random.randint(50,99)
                number2 = random.randint(20,49)
                answer = 0
                print(number1, '+', number2, '=')
                answer = (number1 + number2)
                ans = input('What is the answer?:')
                ans = int(ans)
                answer = int(answer)
                if ans == answer:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeee')
                    print('The answer was:',answer)
                time.sleep(0.2)
                #Algebra X(Subtraction)
                print('Another question!')
                number3 = random.randint(30,40)
                number1 = random.randint(1,10)
                number2 = random.randint(11,29)
                while not number1 == number3 - number2:
                    number1 = random.randint(1,10)
                    number2 = random.randint(11,29)
                    number3 = random.randint(30,40)
                print(number1 , '=', 'x' ,  '-', number2)
                answer = 0
                ans = 0
                ans = input('X = ?:')
                answer = (number1+number2)
                answer = int(answer)
                ans = int(ans)
                if ans == answer:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeeeee')
                    print('The answer was:', answer)
                #Subtraction
                print('Next question:')
                number1 = random.randint(50,99)
                number2 = random.randint(1,49)
                answer = 0
                print(number1, '-', number2, '=')
                answer = (number1 - number2)
                ans = input('What is the answer?:')
                ans = int(ans)
                answer = int(answer)
                if ans == answer:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeee')
                    print('The answer was:',answer)
                time.sleep(0.2)
                #Algebra X (Division)
                print('Another question!')
                number3 = random.randint(30,40)
                number1 = random.randint(1,10)
                number2 = random.randint(11,29)
                while not number1 * number2 == number3:
                    number1 = random.randint(1,10)
                    number2 = random.randint(11,29)
                    number3 = random.randint(30,40)
                print(number1 , '=', 'x',  '/',  number2)
                answer = 0
                ans = 0
                ans = input('X = ?:')
                answer = (number1*number2)
                answer = int(answer)
                ans = int(ans)
                if ans == answer:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeeeee')
                    print('The answer was:', answer)
                #Multiplication
                print('Another question!')
                number1 = random.randint(1,12)
                number2 = random.randint(0,12)
                answer = 0
                print(number1, 'X', number2, '=')
                answer = (number1 * number2)
                ans = input('What is the answer?:')
                ans = int(ans)
                answer = int(answer)
                if answer == ans:
                    print('Correct!')
                    self.score = self.score + 1 # shortcut: self.score += 1
                else:
                    print('Nopeeeee')
                    print('The answer was:',answer)
                time.sleep(0.2)
                #Algebra X (Multiplication)
                print('Another question!')
                number3 = random.randint(10,30)
                number1 = random.randint(20,50)
                number2 = random.randint(1,10)
                while not number1 == number3 * number2:
                    number1 = random.randint(20,50)
                    number2 = random.randint(1,10)
                    number3 = random.randint(10,30)
                print(number1 , '=', 'x', '*',  number2)
                answer = 0
                ans = 0
                ans = input('X = ?:')
                answer = (number1/number2)
                answer = int(answer)
                ans = int(ans)
                if ans == answer:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeeeee')
                    print('The answer was:', answer)
                #Division
                number1 = random.randint(25,75)
                number2 = random.randint(2,10)
                while not number1 % number2 == 0:
                        number1 = random.randint(25,75)
                        number2 = random.randint(2,15)
                print(number1, '/', number2, '=')
                answer = (number1/number2)
                ans = input('What is the answer?:')
                ans = int(ans)
                answer = int(answer)
                if answer == ans:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeeeee')
                    print('The answer was:',answer)
                time.sleep(0.2)
                #Algebra X (Addition)
                print('Another question!')
                number3 = random.randint(1,10)
                number1 = random.randint(30,40)
                number2 = random.randint(11,29)
                while not number1 == number3 + number2:
                    number1 = random.randint(30,40)
                    number2 = random.randint(11,29)
                    number3 = random.randint(1,10)
                print(number1 , '=', 'x',  '+',  number2)
                answer = 0
                ans = 0
                ans = input('X = ?:')
                answer = (number1-number2)
                answer = int(answer)
                ans = int(ans)
                if ans == answer:
                    print('Correct!')
                    self.score = self.score + 1
                else:
                    print('Nopeeeeeee')
                    print('The answer was:', answer)
            print('Bonus Question!')
            number1 = random.randint(1,10)
            number2 = random.randint(5,15)
            number3 = random.randint(1,10)
            ans = 0
            answer = 0
            print('(', number1, '+', number2, ')', 'X', number3)
            ans = input('What is the ANSWER?:')
            answer = ((number1 + number2) * number3)
            ans = int(ans)
            answer = int(answer)
            if ans == answer:
                print('WOW! Incredible! :3')
                self.score = self.score + 2
            else:
                print('W R O N G')
                print('The answer was:', answer)
                self.score = self.score - 1
           
            print('Your score is', m.score)
            if m.score == 82:
                print('Aaaaaaa-ACE! 102.5%')
                print('Wowww, not many people get this score! Bonus points!')
            elif m.score == 80:
                print('Your grade is an A+')
            elif m.score >= 76:
                print('Your grade is an A')
            elif m.score >= 72:
                print('Your grade is an A-')
            elif m.score == 68:
                print('Your grade is an B+')
            elif m.score >= 64:
                print('Your grade is an B')
            elif m.score >= 60:
                print('Your grade is an B-')
            elif m.score == 56:
                print('Your grade is an C+')
            elif m.score >= 52:
                print('Your grade is an C')
            elif m.score >= 48:
                print('Your grade is an C-')
            elif m.score >= 44:
                print('Your grade is an D+')
            elif m.score >= 40:
                print('Your grade is an D')
            elif m.score >= 36:
                print('Your grade is an D-')
            elif m.score < 35:
                print('... FAILURE, F OR LOWER!')
            elif m.score == 0:
                print('u did it on purpose')  
        else:
            print('Ok then, go play the other game')

m = Math(number1, number2, number3)
m.Start()
###Second Game!
#row = right or wrong, 1 is correct, 2 is wrong
play = input('Do you wanna play another game?:')
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
row = 0
value = 0
if play == 'yes' or play == 'yup' or play == 'yersh' or play == 'yes':
    class Game (object):
        def __init__(self, a, b, row, value):
            self.a = a
            self.b = b
            self.value = value
            self.row = row
            self.value = 0
            value = int(value)
            answerr = 0
        def Play(self):
            print('20 questions, t/f(true or false), good luck!')
            for y in range(20):
                a = random.randint(10,100)
                b = random.randint(10,100)
                a = int(a)
                b = int(b)
                f = random.randint(1,5)
                f = int(f)
                g = random.randint(1,5)
                g = int(g)
                c = (a + b)
                c = int(c)
                d = c + f
                d = int(d)
                e = c - g
                e = int(e)
                x = random.randint(1,2)
                x = int(x)
                row = random.randint(1,2)
                if row == 1:
                    print(a, '+', b, '=', c, '?')
                    answerr = input('t/f (true or false):')
                    if answerr == 't':
                        print('Coorrrrecttt')
                        self.value = self.value + 1
                    elif answerr == 'f':
                        print('N00000PEEEE')
                    else:
                        print('Wait wot?')
                        while not answerr == 'f' or 't':
                            answerr = input('t/f (true or false):')
                            if answerr == 't':
                                print('Coorrrrecttt')
                                self.value = self.value + 1
                            elif answerr == 'f':
                                print('N00000PEEEE')
                                print('The answer was true')
                            else:
                                print('Wait wot?')  
                elif row == 2:
                    x = random.randint(1,2)
                    a = random.randint(10,100)
                    b = random.randint(10,100)
                    f = random.randint(1,5)
                    f = int(f)
                    g = random.randint(1,5)
                    g = int(g)
                    c = (a + b)
                    c = int(c)
                    d = c + f
                    d = int(d)
                    e = c - g
                    e = int(e)
                    if x == 1:
                        print(a, '+', b, '=', d)
                        answerr = input('t/f (true or false):')
                        if answerr == 'f':
                            print('Corectt!!!!')
                            self.value = self.value + 1
                        elif answerr == 't':
                            print('NOOOOOPEEEE')
                            print('The answer was false')
                        else:
                            print('Wait wot?')
                    elif x == 2:
                        print(a, '+', b, '=', e)
                        answerr = input('t/f (true or false):')
                        if answerr == 'f':
                            print('Corectt!!!!')
                            self.value = self.value + 1
                        elif answerr == 't':
                            print('NOOOOOPEEEE')
                            print('The answer was false')
                        else:
                            print('Wait wot?')
        z = Game(a,b, row, value)
        z.Play()
        print('Your score final score on the t/f game is', z.value, 'out of 20')
        if z.value == 20:
            print('Your grade is an A+! ACE!!!')
        elif z.value == 19:
            print('Your grade is an A')
        elif z.value == 18:
            print('Your grade is an A-')
        elif z.value == 17:
            print('Your grade is an B+')
        elif z.value == 16:
            print('Your grade is an B')
        elif z.value == 15:
            print('Your grade is an B-')
        elif z.value == 14:
            print('Your grade is an C+')
        elif z.value == 13:
            print('Your grade is an C')
        elif z.value == 12:
            print('Your grade is an C-')
        elif z.value <= 11:
            print(' .... [F]')

else:
    print('Thank you for playing!')

print('-------------------------------------------------------------------------')
print('Thank youuuuuuuu forrrr playinggggg my games!!!!!!!! Idea entirely stolen from Boris lol')



