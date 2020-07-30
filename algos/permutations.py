import time
from threading import Thread
import os

green       = '\u001b[38;2;40;250;40m'
red         = '\u001b[38;2;250;40;40m'
yellow      = '\u001b[38;2;250;200;70m'
clock_color = '\u001b[38;2;245;163;250m'
white       = '\u001b[38;2;255;255;255m'
teal = '\u001b[38;2;63;94;143m'
show_cursor = "\033[?25h"
hide_cursor = "\033[?25l"

def tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330))

def tick_thread():
    return Thread(target = tick)

def low_tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(15/16)))

def low_tick_thread():
    return Thread(target = low_tick)

def high_tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(4/3)))

def high_tick_thread():
    return Thread(target = high_tick)

def med_tick():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(5/4)))

def med_tick_thread():
    return Thread(target = med_tick)

def trade():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.05,330*(4/3)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.05,330*(5/4)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(4/3)))

def trade_thread():
    return Thread(target = trade)

def switch():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.05,330*(15/16)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.05,330*(9/8)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330))

def switch_thread():
    return Thread(target = switch)

def finished():
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330*(5/4)))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.1,330))
    os.system('play -nq -t alsa synth {} sine {}'.format(0.2,330))

def finished_thread():
    return Thread(target = finished)









def next_permutation(x):
    swap_index = len(x) - 2
    while (swap_index >= 0
    and x[swap_index] >= x[swap_index + 1]):
        swap_index -= 1
        if swap_index == -1: return x[::-1]
    for i in reversed(range(swap_index + 1, len(x))):
        if x[i] > x[swap_index]:
            x[swap_index], x[i] = x[i], x[swap_index]
            break
    x[swap_index + 1:] = reversed(x[swap_index + 1:])
    return x








dot = '●'
pointer = '⇃'
lift = '⇡'
drop = '⇣'
swap = '⇋'
reverse = '⇹'

def string_num(x):
    s = yellow
    for i in range(len(x)):
        s += str(hex(x[i]))[-1]
    return s

def string_num_found(x):
    s = green
    for i in range(len(x)):
        s += str(hex(x[i]))[-1]
    return s

def pointer_top(sym,x,a,b = None,first_found = False, second_found = False):
    s = teal
    for i in range(len(x)):
        if i == a:
            if first_found == True:
                s += green
                s += sym
                s += teal
            else:
                s += sym
        elif b != None and i == b:
            if second_found == True:
                s += green
                s += sym
                s += teal
            else:
                s += sym
        else:
            s += dot
    return s

def pointer_swap(x,a,b):
    s = teal
    for i in range(len(x)):
        if i == a or i == b:
            s += green            
            s += swap
            s += teal
        else:
            s += dot
    return s

def lifted(x,a,b):
    s = yellow
    for i in range(len(x)):
        if i == a or i == b:
            s += str(hex(x[i]))[-1]
        else:
            s += ' '
    return s

def missing(x,a,b):
    s = yellow
    for i in range(len(x)):
        if i != a and i != b:
            s += str(hex(x[i]))[-1]
        else:
            s += ' '
    return s

def reverse_tail(x,a):
    s = teal
    for i in range(a+1):
        s += dot
    s += red    
    for i in range(len(x)-a-1):
        s += swap
    return s

def next_vis(x):
    print(hide_cursor)
    basic_top = teal
    for i in range(len(x)):
        basic_top += dot
    print(basic_top)
    print(string_num(x), end  = '\r')
    _ = input('')
    swap_index = len(x) - 2
    while (swap_index >= 0
    and x[swap_index] >= x[swap_index + 1]):
        swap_index -= 1
        search_top = ''
        print(pointer_top(pointer,x,swap_index))
        print(string_num(x))
        _ = input('')
        if swap_index == -1: break
    for i in reversed(range(swap_index + 1, len(x))):
        print(pointer_top(pointer,x,swap_index, first_found = True))
        print(string_num(x))
        _ = input('')
        print(pointer_top(pointer,x,swap_index, i, True))
        print(string_num(x))
        _ = input('')
        if x[i] > x[swap_index]:
            print(pointer_top(pointer,x, swap_index, i,True,True))
            print(string_num(x))
            _ = input('')
            print(pointer_top(lift,x, swap_index, i,True,True))
            print(lifted(x, swap_index, i))
            print(missing(x, swap_index, i))
            _ = input('')
            x[swap_index], x[i] = x[i], x[swap_index]
            print(pointer_top(swap,x, swap_index, i, True,True))
            print(lifted(x, swap_index, i))
            print(missing(x, swap_index, i))
            _ = input('')
            break

    print(pointer_top(drop,x,swap_index, i,True,True))
    print(string_num(x))
    _ = input('')
    x[swap_index + 1:] = reversed(x[swap_index + 1:])
    print(reverse_tail(x,swap_index))
    print(string_num(x))
    _ = input('')


def next_vis_auto(x,delay,sound = True):
    print(hide_cursor)
    basic_top = teal
    for i in range(len(x)):
        basic_top += dot
    print('')
    print(basic_top)
    print(string_num(x), end = '\r')
    #if sound: tick_thread().start()
    time.sleep(delay)
    print('')
    swap_index = len(x) - 2
    while (swap_index >= 0
    and x[swap_index] >= x[swap_index + 1]):
        print('')
        print(pointer_top(pointer,x,swap_index))
        print(string_num(x), end = '\r')
        if sound: tick_thread().start()
        time.sleep(delay)
        print('')
        swap_index -= 1
        if swap_index == -1: return 0
    print('')
    print(pointer_top(pointer,x,swap_index))
    print(string_num(x), end = '\r')
    if sound: tick_thread().start()
    time.sleep(delay)
    print('')
    print('')
    print(pointer_top(pointer,x,swap_index, first_found = True))
    print(string_num(x), end = '\r')
    if sound: med_tick_thread().start()
    time.sleep(delay)
    print('')
    for i in reversed(range(swap_index + 1, len(x))):
        print('')
        print(pointer_top(pointer,x,swap_index, i, True))
        print(string_num(x), end = '\r')
        if sound: tick_thread().start()
        time.sleep(delay)
        print('')
        if x[i] > x[swap_index]:
            print('')
            print(pointer_top(pointer,x, swap_index, i,True,True))
            print(string_num(x), end = '\r')
            if sound: med_tick_thread().start()
            time.sleep(delay)
            print('')
            print(pointer_top(lift,x, swap_index, i,True,True))
            print(lifted(x, swap_index, i))
            print(missing(x, swap_index, i), end = '\r')
            if sound: high_tick_thread().start()
            time.sleep(delay)
            print('')
            x[swap_index], x[i] = x[i], x[swap_index]
            print(pointer_top(swap,x, swap_index, i, True,True))
            print(lifted(x, swap_index, i))
            print(missing(x, swap_index, i), end = '\r')
            if sound: trade_thread().start()
            time.sleep(delay)
            print('')
            break
    print('')
    print(pointer_top(drop,x,swap_index, i,True,True))
    print(string_num(x), end = '\r')
    if sound: low_tick_thread().start()
    time.sleep(delay)
    print('')
    x[swap_index + 1:] = reversed(x[swap_index + 1:])
    print('')
    print(reverse_tail(x,swap_index))
    print(string_num(x), end = '\r')
    if sound: switch_thread().start()
    time.sleep(delay)
    print('')
    print('')
    print(basic_top)
    print(string_num_found(x), end = '\r')
    if sound: finished_thread().start()
    time.sleep(delay*2)
    print('')
    return 1

def full_set(x = [0,1,2,3,4,5,6,7,8,9,10,11,12], delay = 0.5, sound = True):
    a = 1
    while a == 1:
        a = next_vis_auto(x, delay, sound)
