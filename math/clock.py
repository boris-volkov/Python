import time

tm = time.localtime( time.time() )
sec = tm.tm_hour*60*60
sec += tm.tm_min*60
sec += tm.tm_sec
print('\u001b[93m')

#f'{key:20s}'

#sec = 0

while 1:
    normal = (' ' + str(sec//(60*60)%24) + ":" + str((sec//60)%60) + ":" + str(sec%60))
    print(f'{normal:>20}')
    hexa = (' ' + str(hex(sec))[2:])
    print(f'{hexa:>20}')
    decimal = (' ' + str(sec))
    print(f'{decimal:>20}')
    binary = (' ' + str(bin(sec))[2:])
    print(f'{binary:>20}')
    percent = (' ' + str( round(100*sec/(24*60*60))) + '%')
    print(f'{percent:>20}', end = '\r')
    time.sleep(1)
    sec += 1


