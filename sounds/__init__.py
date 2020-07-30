from threading import Thread
import os

A = 436.05/4
A_sharp = 490.55/4
B = 523.25/4
C = 261.63/2
C_sharp = 272.54/2
D = 294.33/2
D_sharp = 313.96/2
E = 327.03/2
F = 348.83/2
F_sharp = 367.92/4
G = 392.44/4
G_sharp = 418.6/4

tonic = 1
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
octave = 2

major_scale = [tonic, whole_tone, major_third, perfect_fourth, perfect_fifth, major_sixth, major_seventh]

harmonic_minor_scale = [tonic, whole_tone, minor_third, perfect_fourth, perfect_fifth, minor_sixth, major_seventh]

aeolian_mode = [tonic, whole_tone, minor_third, perfect_fourth, perfect_fifth, minor_sixth, minor_seventh]

major_arpeggio = [tonic, major_third, perfect_fifth]

chromatic_scale = [tonic, semitone, whole_tone, minor_third, major_third, perfect_fourth, tritone, perfect_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh]

algerian_scale = [tonic, whole_tone, minor_third, tritone, perfect_fifth, minor_sixth, major_seventh]

bebop_dominant_scale = [tonic, whole_tone, major_third, perfect_fourth, perfect_fifth, major_sixth, minor_seventh, major_seventh]

blues_scale = [tonic, minor_third, perfect_fourth, tritone, perfect_fifth, minor_seventh]

enigmatic_scale = [tonic,semitone,major_third,tritone,minor_sixth,major_sixth, major_seventh]

gypsy_scale = [tonic, whole_tone, minor_third, tritone, perfect_fifth, minor_sixth, minor_seventh]

harajoshi_scale = [tonic, major_third, tritone, perfect_fifth, major_seventh]

hungarian_gypsy_scale = [tonic, whole_tone, minor_third, tritone, perfect_fifth, minor_sixth, major_seventh]

hungarian_minor_scale = [tonic, whole_tone, minor_third, tritone, perfect_fifth, minor_sixth, major_seventh]

insen_scale = [tonic, semitone, perfect_fourth, perfect_fifth, minor_seventh]

iwato_scale = [tonic, semitone, perfect_fourth, tritone, minor_seventh]

persian_scale = [tonic, semitone, major_third, perfect_fourth, tritone, minor_sixth, major_seventh]

prometheus_scale = [tonic, whole_tone, major_third,tritone, major_sixth, minor_seventh]

yo_scale = [tonic, minor_third, perfect_fourth, perfect_fifth, minor_seventh]

dorian_scale = [tonic, whole_tone, minor_third, perfect_fourth, perfect_fifth, major_sixth, minor_seventh]

double_harmonic_scale = [tonic, semitone, major_third, perfect_fourth, perfect_fifth, minor_sixth, major_seventh]

flamenco_mode = [tonic, semitone, major_third, perfect_fourth, perfect_fifth, minor_sixth, major_seventh]

istrian_scale = [tonic, semitone, minor_third, major_third, tritone, perfect_fifth]

ukranian_dorian_scale = [tonic, whole_tone, minor_third, tritone, perfect_fifth, major_sixth, minor_seventh]

minor_pentatonic_scale = [tonic, minor_third, perfect_fourth, perfect_fifth, minor_seventh] #same as the yo scale

major_pentatonic_scale = [tonic, whole_tone, major_third, perfect_fifth, major_sixth]

egyptian_pentatonic_scale = [tonic, whole_tone, perfect_fourth, perfect_fifth, minor_seventh]

man_gong_scale = [tonic, minor_third, perfect_fourth, minor_sixth, minor_seventh]


def octaves(scale, n):
    first_octave = scale
    notes = []
    for i in range(n):
        notes = notes + [x*(2**i) for x in first_octave]
    return notes

def play_sawtooth(duration,frequency):
    def play():
        os.system('play --bits=64 -nq -c1 -t alsa synth {} sawtooth {} channels 2 gain -10'.format(duration,frequency))
    def play_thread():
        return Thread(target = play)
    play_thread().start()

def play_exp(duration,frequency):
    def play():
        os.system('play --bits=64 -nq -c1 -t alsa synth {} exp {} channels 2 gain -10'.format(duration,frequency))
    def play_thread():
        return Thread(target = play)
    play_thread().start()

def play_sine(duration, frequency):
    def play():
        os.system('play --bits=64 -nq -c1 -t alsa synth {} sine {} channels 2'.format(duration,frequency))
    def play_thread():
        return Thread(target = play)
    play_thread().start()

def play_trap(duration, frequency):
    def play():
        os.system('play --bits=64 -nq -c1 -t alsa synth {} trapezium {} channels 2 gain -10'.format(duration,frequency))
    def play_thread():
        return Thread(target = play)
    play_thread().start()

def play_square(duration, frequency):
    def play():
        os.system('play --bits=64 -nq -c1 -t alsa synth {} square {} channels 2 gain -10'.format(duration,frequency))
    def play_thread():
        return Thread(target = play)
    play_thread().start()

def play_pluck(duration, frequency):
    def play():
        os.system('play --bits=64 -nq -c1 -t alsa synth {} pluck {} channels 2 gain -10'.format(duration,frequency))
    def play_thread():
        return Thread(target = play)
    play_thread().start()

def list_sounds():
    print("sawtooth, sine, trap, square, exp, pluck")

def sawtooth(d,f):
    os.system('play --bits=64 -nq -c1 -t alsa synth {} sawtooth {} channels 2 gain -10'.format(d,f))

def sine(d,f):
    os.system('play --bits=64 -nq -c1 -t alsa synth {} sine {} channels 2 gain -10'.format(d,f))

def trap(d,f):
    os.system('play --bits=64 -nq -c1 -t alsa synth {} trapezium {} channels 2 gain -10'.format(d,f))

def square(d,f):
    os.system('play --bits=64 -nq -c1 -t alsa synth {} square {} channels 2 gain -10'.format(d,f))

def exp(d,f):
    os.system('play --bits=64 -nq -c1 -t alsa synth {} exp {} channels 2 gain -10'.format(d,f))

def pluck(d,f):
    os.system('play --bits=64 -nq -c1 -t alsa synth {} pluck {} channels 2 gain -10'.format(d,f))


# this needs a lot of fixing if i want it to return a thread
def melody(M,tonic,sound):
    """input List[(dur,freq)],tonic, sound type"""
    def notes():
        for note in M:
            sound(note[0],tonic*note[1])
    def notes_thread():
        return Thread(target = notes)
    notes_thread().start()
