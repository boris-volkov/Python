import time
from threading import Thread
import os
import math

adder_bits = 32
cyan        = '\u001b[96m'
black       = '\u001b[30m'
green       = '\u001b[38;2;60;255;60m'
red         = '\u001b[38;2;250;40;100m'
yellow      = '\u001b[38;2;250;200;70m'
clock_color = '\u001b[38;2;245;163;250m'
teal = '\u001b[38;2;63;94;143m'

one = "▉"
zero = " "

print(yellow)

def lights(x):
    row = ""
    for i in reversed(range(16)):
        if x & 2**i:
            row += one
        else:
            row += zero
    return row

def lights_adder(x):
    row = ""
    for i in reversed(range(adder_bits)):
        if x & 2**i:
            row += one
        else:
            row += zero
    return row

def lights_counter(x):
    row = ""
    for i in reversed(range(16)):
        if x & 2**i:
            row += one
        else:
            row += zero
    return row

def count_binary():
    i = 0
    print("\033[?25l")
    while 1:
        print(yellow + '⇃', end = "") 
        print(teal + '⇃'*15) 
        print(yellow + lights_counter(i))
        print(yellow + lights_counter(i))
        print(yellow + lights_counter(i), end = '\r')
        i += 1
        time.sleep(1)

def tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330))

def high_tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(3/2)))

def low_tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(2/3)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(2/3)))

def finished():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(5/4)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(3/2)))

def finished_thread():
    return Thread(target = finished)

def low_tick_thread():
    return Thread(target = low_tick)

def tick_thread():
    return Thread(target = tick)

def high_tick_thread():
    return Thread(target = high_tick)
    
def power_2(n):
    return ((n != 0) and ((n & (n-1)) == 0))

def learn_binary():
    i = 0
    print("\033[?25l")
    print(yellow, end = '')
    while 1:
        decimal = str(i)
        print(f'{decimal:>16}')
        if power_2(i):
            print(teal + '⇃'*int(15-math.log(i,2)), end = '')
            print(green + '⇃', end = "") 
            print(teal + '⇃'*int(math.log(i,2)))
        else:            
            print(teal + '⇃'*16) 
        print(yellow + lights_counter(i))
        print(yellow + lights_counter(i), end = '\r')
        i += 1
        _ = input("")
        if power_2(i):
            high_tick_thread().start()
            print(green, end = '')
        else:
            tick_thread().start()
            print(yellow, end = '')

def clock():
    print("\033[?25l")
    while 1:
        now = time.localtime(time.time())
        print(yellow + '⇃', end = "") 
        print(teal + '⇃'*15 + yellow) 
        print(lights(now.tm_hour))
        print(lights(now.tm_min))
        print(lights(now.tm_sec), end = '\r')
        time.sleep(1) 
        tick_thread().start()

def add(a,b):
    print('\n')
    while b:
        down_string = ''
        for i in range(adder_bits):
            if (b>>i)&1:
                down_string = yellow + '⇃' + down_string
            else:
                down_string = black + '⇃' + down_string
                
        print(down_string + yellow) 
        print(lights_adder(b))
        print(lights_adder(a) + '\n'*2)
        tick_thread().start()
        carry = a&b
        _ = input('')
        add_string = ''
        for i in range(adder_bits):
            if (b>>i)&1 and not (a>>i)&1:
                add_string = (yellow + '⇣') + add_string 
            elif (carry>>i)&1:
                add_string =  (teal + '⇡') + add_string
            else:
                add_string = black + '⇃' + add_string
        a = a^b
        print(add_string)
        print(teal + lights_adder(carry))
        print(yellow + lights_adder(a) + '\n'*2)
        tick_thread().start()
        b = carry<<1
        _ = input('')
        carry_string = ''
        for i in range(adder_bits):
            if (b>>i)&1:
                carry_string = teal + '↼' + carry_string
            else:
                carry_string = black + '⇃' + carry_string
        if b == 0:
            print(red + '↚'*adder_bits) 
            low_tick_thread().start()
        else:
            print(carry_string) 
            tick_thread().start()
        print(teal + lights_adder(b))
        print(yellow + lights_adder(a) + '\n'*2)
        _ = input('')
        
    print(black + '⇃'*adder_bits + yellow) 
    print(green + lights_adder(a)+ '\n'*2)
    finished_thread().start()
    _ = input('')

