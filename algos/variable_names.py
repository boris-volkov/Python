def var_maker(n):
    string = []
    while n >= 26:
        string.append( chr(n % 26 + 65 ) )
        n //= 26
        n -= 1
    string.append( chr(n + 65) )
    return ''.join(string)

c = 0
from time import sleep
while 1:
    sleep(.5)
    print(c, var_maker(c))
    c += 1


