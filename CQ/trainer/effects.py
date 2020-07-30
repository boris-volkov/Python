import os
from threading import Thread

frog        = '\U0001F438'

#---------------------------------------------------Game Sounds
dur1 = 0.05
dur2 = 0.1

semitone = (16/15)
whole_tone = (9/8)
minor_third = (6/5)
major_third = (5/4)
perfect_fourth = (4/3)
tritone = (7/5)
perfect_fifth = (3/2)
minor_sixth = (8/5)
major_sixth = (5/3)
minor_seventh = (9/5)
major_seventh = (15/8)

freq = 220
def success_sound():
    freq1 = 2*freq
    freq2 = 2*freq*whole_tone
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq2))

def name_entered():
    freq1 = freq*(15/16)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(.25,freq1))

def name_thread():
    return Thread(target = name_entered)

def success_thread():
    return Thread(target = success_sound)

def speed_bonus_sound():
    freq1 = 2*freq
    freq3 = 2*freq*major_third
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq3))

def speed_thread():
    return Thread(target = speed_bonus_sound)

def fail_sound():
    freq1 = freq * (15/16)
    freq2 = freq * (2/3)
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur1,freq1))
    os.system('play -nq -t alsa synth {} trapezium {}'.format(dur2,freq2))

def fail_thread():
    return Thread(target = fail_sound)

def null_sound():
    dur1 = .1
    freq1 = 564
    os.system('play -nq -t alsa synth {} trapezium {} tremolo 10 40 '.format(dur1,freq1))

def empty_thread():
    return Thread(target = null_sound)

def intro_song():
    durs =      [.5, .5  , .125 , .125 , .125 , .5]
    freqs= freq*np.array([1 ,(15/16),(6/5),(6/5),(2/3),  1])
    bass = freq*np.array([(1/2),(2/3),(3/5),(3/5), (1/2), (1/2) ])
    for i in range(len(freqs)):
        os.system('play -nq -t alsa synth {} sine {} trapezium {}'.format(durs[i], bass[i] ,freqs[i]))

def intro_thread():
    return Thread(target = intro_song)

def finish_song():
    durs =     [.5, 0.25, 0.25, .5]
    freqs=freq*np.array([1.5 , 1.25, .935,  1])
    for i in range(len(freqs)):
        os.system('play -nq -t alsa synth {} trapezium {}'.format(durs[i],freqs[i]))

