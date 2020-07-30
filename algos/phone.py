import enchant

letters = {
            2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz'
        }

legal_digits = '23456789'

def name(n):
    string = []
    while n >= 26:
        string.append( chr(n % 26 + 65 ) )
        n //= 26
        n -= 1
    string.append( chr(n + 65) )
    return ''.join(string)

class PhoneWords(object):
    L = []
    def combos(self, digits: str):
        if not digits or any(d not in legal_digits for d in digits):
            return 'what are you doing?'
        names = []
        loops = []
        for i,j in enumerate(digits):
            x = name(i)
            names.append(x)
            loops.append(' for '+x+' in letters['+j+'] ')
        code = 'self.L = [' + '+'.join(names) + ''.join(loops) + ']'
        exec(code)
        return self.L

checker = enchant.Dict()
def word_checker(word):
    print(word)
    if word == '':
        return True
    for i in range(2, len(word)+1):
        if checker.check(word[:i]):
            if word_checker(word[i:]):
                return True
    return False

test = '9799949'
combiner = PhoneWords()
l = combiner.combos(test)
print(l)
real = [word for word in l if word_checker(word)]
print(real)
