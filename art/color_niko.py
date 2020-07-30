import colors as c
from time import sleep

print(c.hide_cursor)
string = 'nikolai_volkov'

while 1:
    print(c.rand_f())
    print(c.rand_b())
    print('\n'*20)
    for i in range(len(string)+1):
        print(string[:i], end = '\r')
        sleep(1)

