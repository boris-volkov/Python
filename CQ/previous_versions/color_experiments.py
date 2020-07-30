import time, sys

#figure out different ways to encode color printing:
#   '\033[95m'   is one way
# and 'u\u001b[95m' is another
# but putting these character strings into the prints will do stuff


def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write("\033[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print()


loading()

#this is a script that takes stdout and reroutes it to a file

temp = sys.stdout
sys.stdout = open('log.txt','w')
print("testing123")
print("another line")
sys.stdout.close()
sys.stdout = temp
print("back to normal")


#more experiments with stdout, showing that the print
# waits for the to buffer flush

import time
import sys

for i in range(10):
    print i
    if i == 5:
        print "Flushing buffer"
        sys.stdout.flush()
    time.sleep(1)

for i in range(10):
    print i,
    if i == 5:
        print "Flushing buffer"
        sys.stdout.flush()
