from random import randint
import colors
import time

directory = '/home/boris/Documents/Books'
book = 'homer_iliad'
#  book = 'bible'


with open(directory + '/' + book + '.txt') as file:
    line_array = []
    for line in file:
        line_array.append(line)

def mean(A):
    if A:
        total = 0
        for a in A:
            total += a
        mean = total/len(A)
        return mean
    return 0

cpm = []

def check_word(word):
    global cpm
    while 1:
        print(colors.clear_screen)
        print(colors.rgb(0,0,0))
        print("characters per minute: " + str(mean(cpm)) + '\n'*4) 
        print(colors.yellow)
        begin = time.time()
        test = input(str(word) + colors.cyan + '[' + '\n')
        if str(test) == str(word):
            elapsed = time.time() - begin
            cpm.append(len(test)*60/elapsed)
            return

print(colors.clear_screen)
_ = input(' When you press enter, you will start typing lines from the Iliad.\n The entire line must match or else you must repeat it.')
start_line = randint(1,20000)
for i,phrase in enumerate(line_array[start_line:]):
    if len(phrase) > 1:
        check_word(phrase.strip())
            
