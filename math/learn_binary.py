import time
from threading import Thread
import os
import math
from random import randint
import sounds as s


cyan        = '\u001b[96m'
black       = '\u001b[30m'
green       = '\u001b[38;2;60;255;60m'
red         = '\u001b[38;2;250;40;40m'
yellow      = '\u001b[38;2;250;200;70m'
clock_color = '\u001b[38;2;245;163;250m'
white       = '\u001b[38;2;255;255;255m'
teal = '\u001b[38;2;63;94;143m'
show_cursor = "\033[?25h"
hide_cursor = "\033[?25l"

one = "▉"
zero = " "

print(yellow)
print("\033[?25l")

def lights(x, w = 16):
    row = ""
    for i in reversed(range(w)):
        if x & 2**i:
            row += one
        else:
            row += zero
    return row

def lights_adder(x, bits):
    row = ""
    for i in reversed(range(bits)):
        if x & 2**i:
            row += one
        else:
            row += zero
    return row

def lights_counter(x, bits = 16):
    row = ""
    for i in reversed(range(bits)):
        if x & 2**i:
            row += one
        else:
            row += zero
    return row

def count():
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

def count_day(bits = 16):
    now = time.localtime( time.time() )
    sec = now.tm_sec
    sec += now.tm_min*60
    sec += now.tm_hour*60*60
    sec = round(sec*(2**bits)/(24*60*60))
    binary_second = (24*60*60)/(2**bits)
    i = sec
    print(hide_cursor)
    while 1:
        print(yellow + '⇃', end = "") 
        print(teal + '⇃'*(bits-1)) 
        print(yellow + lights_counter(i, bits))
        print(yellow + lights_counter(i, bits))
        print(yellow + lights_counter(i, bits), end = '\r')
        i += 1
        time.sleep(binary_second)

def count():
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

def med_tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(3/2)))

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

def med_tick_thread():
    return Thread(target = med_tick)

def tick_thread():
    return Thread(target = tick)

def high_tick_thread():
    return Thread(target = high_tick)
    
def power_2(n):
    return ((n != 0) and ((n & (n-1)) == 0))

def binary_note(x, base = s.C, scale = s.major_scale ):
    notes = s.octaves(scale,16//len(scale)+1)
    f = base
    a = x ^ (x - 1)
    biggest_bit = 0
    while a:
        a = a>>1
        biggest_bit += 1
    s.play_sine(0.1, base*notes[biggest_bit-1])


def learn(mode = s.blues_scale):
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
        binary_note(i, scale = mode )
        if power_2(i):
            print(green, end = '')
            print()
        else:
            print(yellow, end = '')
            print()

def clock(w = 16):
    print("\033[?25l")
    width = w
    while 1:
        now = time.localtime(time.time())
        print(yellow + '⇃', end = "") 
        print(teal + '⇃'*(width-1) + yellow) 
        print(lights(now.tm_hour,width))
        print(lights(now.tm_min,width))
        print(lights(now.tm_sec,width), end = '\r')
        time.sleep(1) 
        tick_thread().start()

def add(a,b, bits = 16):
    if bits == 34:
        blanks = 2
    elif bits == 16:
        blanks = 0
    else:
        blanks = 2
    adder_bits = bits
    print(hide_cursor)
    while b:
        down_string = ''
        for i in range(adder_bits):
            if (b>>i)&1:
                down_string = yellow + '⇃' + down_string
            else:
                down_string = black + '⇃' + down_string
                
        print(down_string + yellow) 
        print(lights_adder(b, bits))
        print(lights_adder(a, bits) + '\n'*blanks)
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
        print(teal + lights_adder(carry, bits))
        print(yellow + lights_adder(a, bits) + '\n'*blanks)
        med_tick_thread().start()
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
        print(teal + lights_adder(b, bits))
        print(yellow + lights_adder(a, bits) + '\n'*blanks)
        _ = input('')
        
    print(white + '⇃'*adder_bits + yellow) 
    print(green + lights_adder(a, bits)+ '\n'*blanks)
    finished_thread().start()
    _ = input('')
    print(show_cursor)

def add_auto(a,b, bits = 16):
    if bits == 34:
        blanks = 2
    elif bits == 16:
        blanks = 0
    else:
        blanks = 2
    adder_bits = bits
    print(hide_cursor)
    while b:
        down_string = ''
        for i in range(adder_bits):
            if (b>>i)&1:
                down_string = yellow + '⇃' + down_string
            else:
                down_string = black + '⇃' + down_string
                
        print(down_string + yellow) 
        print(lights_adder(b, bits))
        print(lights_adder(a, bits) + '\n'*blanks)
        tick_thread().start()
        carry = a&b
        time.sleep(1)
        print('\n')
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
        print(teal + lights_adder(carry, bits))
        print(yellow + lights_adder(a, bits) + '\n'*blanks)
        med_tick_thread().start()
        b = carry<<1
        time.sleep(1)
        print('\n')
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
        print(teal + lights_adder(b, bits))
        print(yellow + lights_adder(a, bits) + '\n'*blanks)
        time.sleep(1)
        print('\n')
        
    print(white + '⇃'*adder_bits + yellow) 
    print(green + lights_adder(a, bits)+ '\n'*blanks)
    finished_thread().start()
    time.sleep(1)

def add_random_auto(bits = 16):
    while 1:
        add_auto(randint(1,2**(bits-1)), randint(1, 2**(bits-1)), bits)
        time.sleep(1)

def add_random(bits = 16):
    add(randint(1,2**(bits-1)), randint(1, 2**(bits-1)), bits)

if __name__ == '__main__':
    clock()
