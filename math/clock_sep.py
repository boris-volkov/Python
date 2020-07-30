import time
from fractions import Fraction
import os

tm = time.localtime( time.time() )
sec = tm.tm_hour*60*60
sec += tm.tm_min*60
sec += tm.tm_sec
cyan        = '\u001b[96m'
yellow      = '\u001b[93m'
red         = '\u001b[91m'
fraction_color = '\u001b[30;1m'
date_color = '\u001b[32;0m'
weekdays = ['monday','tuesday','wednesday','thursday', 'friday', 'saturday', 'sunday']

while 1:
    os.system('clear')
    print(date_color, end = '')
    print(' ' + str(tm.tm_year) + ':' + str(tm.tm_mon) + ':' + str(tm.tm_mday))
    normal = (' ' + str(sec//(60*60)%24) + ":"  +  str((sec//60)%60) +  ":" +  str(sec%60))
    print(red, end = '\r')
    print(f'{normal:>25}', end = '\r')
    print(date_color, end = '')
    print(' ' + weekdays[tm.tm_wday])
    print(yellow, end = '\r')
    hexa = (' ' + str(hex(sec//(60*60)%24))[2:] + ":" + str(hex(sec//60%60))[2:] + ":" + str(hex(sec%60))[2:])
    print(f'{hexa:>25}')
    binary = (' ' + str(bin(sec//(60*60)%24))[2:] + ":" + str(bin(sec//60%60))[2:] + ":" + str(bin(sec%60))[2:])
    print(f'{binary:>25}')
    decimal = (' ' + str((sec%10**5)//10**4)+':'+str((sec%10**4)//10**3)+':'+str((sec%10**3)//10**2)+':'+str((sec%10**2)//10)+':'+str(sec%10))
    print(f'{decimal:>25}')
    percent = (' ' + str((100*(100*sec/(24*60*60))//1)/100) + '%')
    print(cyan, end = '\r')
    fraction_of_day = Fraction(sec, 86400)
    frac_string = (str(fraction_of_day.numerator) + ':' + str(fraction_of_day.denominator))
    print(f'{percent:>25}', end = '\r')
    print(fraction_color, end = '\r')
    print(' ' + frac_string)        
    print(yellow, end = '\r')
    time.sleep(1)
    sec += 1


