from threading import Thread
import os
import numpy as np
import random
import math
import time
import colors

main_tonic = 110
def set_main_tonic(x):
	global main_tonic
	main_tonic = x

num_measures = 108   #measures in song
bpm = 3      #beats per measure (seconds)
bass_count = num_measures*bpm

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

notes = {'C#':C_sharp, 'D ' : D, 'D#' : D_sharp, 'E ' : E, 'F ' : F, 'F#' : F_sharp, 'G ' : G, 'G#' : G_sharp, 'A ' : A, 'A#' : A_sharp, 'B ' : B, 'C ' : C}

ordered_notes = {'C ' : C, 'G ' : G, 'D ' : D, 'A ' : A,'E ' : E,'B ' : B, 'F#' : F_sharp,'C#' : C_sharp,'G#': G_sharp,'D#' : D_sharp,'A#' : A_sharp,'F ' :  F}

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

chromatic_scale = [tonic, semitone, whole_tone, minor_third, major_third, perfect_fourth, tritone, perfect_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh]

major_scale = [tonic, whole_tone, major_third, perfect_fourth, perfect_fifth, major_sixth, major_seventh]

harmonic_minor_scale = [tonic, whole_tone, minor_third, perfect_fourth, perfect_fifth, minor_sixth, major_seventh]

aeolian_mode = [tonic, whole_tone, minor_third, perfect_fourth, perfect_fifth, minor_sixth, minor_seventh]

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

scales = {'harmonic_minor_scale' :harmonic_minor_scale, 'aeolian_mode' :  aeolian_mode, 'major_scale' :  major_scale, 'algerian_scale' :  algerian_scale, 'bebop_dominant_scale' :  bebop_dominant_scale, 'blues_scale' : blues_scale, 'enigmatic_scale' :  enigmatic_scale, 'gypsy_scale' :  gypsy_scale, 'harajoshi_scale' : harajoshi_scale, 'hungarian_gypsy_scale' : hungarian_gypsy_scale, 'hungarian_minor_scale' : hungarian_minor_scale, 'insen_scale' : insen_scale, 'iwato_scale' : iwato_scale, 'persian_scale' : persian_scale, 'prometheus_scale' : prometheus_scale, 'yo_scale' : yo_scale, 'dorian_scale' : dorian_scale, 'double_harmonic_scale' : double_harmonic_scale, 'flamenco_mode' : flamenco_mode, 'istrian_scale' : istrian_scale, 'ukranian_scale' : ukranian_dorian_scale}

major_scales = {'major_scale' : major_scale, 'bebop_dominant_scale' : bebop_dominant_scale, 'enigmatic_scale' :  enigmatic_scale, 'harajoshi_scale' : harajoshi_scale, 'persian_scale' : persian_scale, 'premetheus_scale' : prometheus_scale, 'flamenco_mode' : flamenco_mode}

minor_scales = {'harmonic_minor_scale' : harmonic_minor_scale,'aeolian_mode' : aeolian_mode, 'algerian_scale' : algerian_scale, 'blues_scale' :  blues_scale, 'gypsy_scale' : gypsy_scale, 'hungarian_gypsy_scale' : hungarian_gypsy_scale, 'hungarian_minor_scale' : hungarian_minor_scale, 'yo_scale' : yo_scale, 'dorian_scale' : dorian_scale, 'ukranian_dorian_scale' : ukranian_dorian_scale, 'istrian_scale' : istrian_scale, 'double_harmonic_scale' : double_harmonic_scale}

pentatonic_scales = {'dorian' : dorian_scale, 'yo_scale': yo_scale, 'iwato_scale' : iwato_scale, 'insen_scale': insen_scale, 'harajoshi_scale': harajoshi_scale, 'minor_pentatonic_scale' : minor_pentatonic_scale, 'major_pentatonic_scale' : major_pentatonic_scale, 'egyptian_pentatonic_scale' : egyptian_pentatonic_scale, 'man_gong_pentatonic_scale' : man_gong_scale}

main_scale = []
def set_main_scale(x):
    global main_scale
    main_scale = x
def get_main_scale():
    return main_scale

def noise(x):
    return 0
#    if x == 1:
#        return np.random.normal(0, 0.025)
#    return np.random.normal(0, .05, x)

def play(d,f):
    os.system('play --bits=32 -nq -c1 -t alsa synth {} pluck {} channels 2 gain -10'.format(d,f))

def play_bass(d,f):
    os.system('play --bits=32 -nq -c2 -t alsa synth {} pluck {} channels 2 gain -1 fade h 1'.format(d,f))

def melody(D,F,tonic):
    for i in range(len(F)):
        play(D[i],tonic*F[i])

def scale(dur, scale, tonic, octaves):
    for j in range(1,octaves+1):
        for i in range(len(scale)):
            play(dur,tonic*scale[i]*2**j)
    play(dur,tonic*2**(octaves+1))        
    for j in range(octaves,0,-1):
        for i in range(len(scale)-1,-1,-1):
            play(dur,tonic*scale[i]*2**j)


def multi_octave_scale(s, octaves = 3, tonic = 65.41):
    for i in range(2,5):
        scale(2**(-i), s , tonic , octaves)

#multi_octave_scale(double_harmonic_scale, 4, tonic = C_sharp/2)

def measure(beats):
    times = [3/2, 1, 1/2, 1/4, 1/4, 1/8, 1/8, 1/3, 1/6, 2/3]
    mes = []
    while True:
        mes.append(random.choice(times)+noise(1))
        if math.isclose(sum(mes),beats, abs_tol = 0.1):
            return mes
        if sum(mes) > beats:
            mes = []

def measure_bass(beats):
    times = [bpm, bpm/2]
    mes = []
    while True:
        mes.append(random.choice(times)+noise(1))
        if math.isclose(sum(mes),beats, abs_tol = 0.1):
            return mes
        if sum(mes) > beats:
            mes = []

def random_walk(length, limit):
	a = [0]*length
	for i in range(1,length):
		n = random.random()
		if n > .85 : a[i] = min(a[i-1] + 1 , limit)
		elif n > .15 : a[i] = a[i-1]		
		else:       a[i] = max(a[i-1] - 1 , 0)
	return a

def random_walk_jump(length, limit):
    a = [0]*length
    a[0] = round(limit/2)
    for i in range(1,length):
        n = random.random()
        if   n > .95 :  a[i] = min(a[i-1] + 3,limit)
        elif n > .90:  a[i] = min(a[i-1] + 2,limit)
        elif n > .60:  a[i] = min(a[i-1] + 1,limit)
        elif n > .40 :  a[i] = a[i-1]
        elif n > .10:  a[i] = max(a[i-1] - 1,0)
        elif n > .05:  a[i] = max(a[i-1] - 2,0)
        else:          a[i] = max(a[i-1] - 3,0)
    return a

def octaves(scale, n):
    first_octave = scale
    notes = []
    for i in range(n):
        notes = notes + [x*(2**i) for x in first_octave]
    return notes

def bumblebee(note, length, tonic):
    scale = octaves(chromatic_scale, 5)
    print(scale)
    walk = random_walk(length, len(scale))
    print(walk)
    for i in range(len(walk)):
        play(note, tonic*scale[walk[i]])

#bumblebee(1/28, 100 , 70)    

def random_song(tonic, scale, measures, beats, n_oct = 3):
    notes = octaves(scale, n_oct)
    play(1,tonic)
    for i in range(measures):
        mes = measure(beats)
        for j in mes:
            play(j, tonic*notes[random.randint(0,len(scale)-1)])
    play(2,tonic)

def bass_major(d = bpm*2,a = main_tonic):
    for i in range(round(bass_count/d)):
        if i%6 == 5:
            play(d,a*perfect_fifth)
        elif i%6 == 4:
            play(d,a*major_third)
        elif i%6 == 0:
            play(d/2,a/2)
            play(d/2,a/2)
        else: 
            play(d,a)
    play(d*4,a/2)

def bass_minor(d = bpm*2,a = main_tonic):
    for i in range(round(bass_count/d)):
        if i%6 == 5:
            play(d,a*perfect_fifth)
        elif i%6 == 4:
            play(d,a*minor_third)
        elif i%6 == 0:
            play(d/2,a/2)
            play(d/2,a/2)
        else: 
            play(d,a)
    play(d*4,a/2)

def bass_enigmatic(d = bpm*2,a = main_tonic):
    for i in range(round(bass_count/d)):
        if i%6 == 0:
            play(d/2,a/2)
            play(d/2,a/2)
        else: 
            play(d,a)
    play(d*4,a/2)

def bass_thread():
    return Thread(target = bass_major)

def bass_thread_minor():
    return Thread(target = bass_minor)

def enigmatic_thread():
    return Thread(target = bass_enigmatic)

def random_bass(scale = get_main_scale(), tonic = main_tonic, measures_in_song = num_measures, beats = bpm, n_oct = 4):
    print(scale)
    print(tonic)    
    notes = [x/2 for x in scale]
    notes = notes + [2]
    measures = []
    for i in range(measures_in_song):
        mes = measure_bass(beats)
        measures = measures + mes
    melody_pattern = random_walk_jump(len(measures), len(notes)-1)
    melody = []
    for i in range(len(melody_pattern)):
        melody.append(notes[melody_pattern[i]])
    play(1,tonic/2)
    for j in range(len(measures)):
        play(measures[j], tonic*melody[j]+noise(1))
    play(3,tonic/2)

def random_bass_thread():
    return Thread(target = random_bass)

def random_song_walk(scale = get_main_scale(), tonic = main_tonic, measures_in_song = num_measures, beats = bpm, n_oct = 3):
    #print(tonic)    
    #print(scale)
    notes = octaves(scale, n_oct)
    notes = notes + [2**(n_oct)]
    measures = []
    for i in range(measures_in_song):
        mes = measure(beats)
        measures = measures + mes
    melody_pattern = random_walk_jump(len(measures), len(notes)-1)
    melody = []
    for i in range(len(melody_pattern)):
        melody.append(notes[melody_pattern[i]])
    #play(1,main_tonic*2)
    for j in range(len(measures)):
        play(measures[j], tonic*melody[j]+noise(1))
    play(2,tonic)

#--------------------------------------------------------------------------------------JTS methods

cyan        = '\u001b[96m'
yellow      = '\u001b[93m'
green       = '\u001b[92m'
screen      = '\033[2J'

def just_tempered_synth_double_thread(scales):
    """Plays a scale and tune in each key/scale combination    
       Input is a dict of scales"""

    print(screen + yellow)
    print('Hello, I am a program called the\n' + cyan + '       JUST_TEMPERED_SYNTHESIZER' + yellow + '\n  ( as opposed to the Well-Tempered Clavier by JS Bach )\nI am a far more humble composer, but I can play in tune,\nand I can play fast, and I don\'t get tired\n  ( as long as you keep me plugged in! )\nImitating Bach, I will be playing music in {} scales,\nin each key, but using '.format(len(scales))+cyan+'Just Intonation'+yellow+'.\nWhat you are hearing is randomly generated,\n  ( within some sensible constraints )\nI do not know what music is, but I hope you enjoy mine.\nPardon its quality, I am only a machine.\n\n Current ' + green + 'key : ' + cyan + 'scale  =' )
    start = time.perf_counter()
    for scale_name, s in scales.items():
        for note_name , note in ordered_notes.items():
            print(' '*9 + green + note_name + '  : ' + cyan + scale_name, end = '\r')    
            def random_bass(scale = s, tonic = note,
                measures_in_song = num_measures, beats = bpm):
                notes = [1,1/2]
                if minor_third in scale: notes += [minor_third, minor_third/2]
                if major_third in scale: notes += [major_third, major_third/2]
                if perfect_fifth in scale: notes += [perfect_fifth, perfect_fifth/2]
                notes = sorted(notes)
                measures = []
                for i in range(measures_in_song):
                    mes = measure_bass(beats)
                    measures += mes
                melody_pattern = random_walk(len(measures), len(notes)-1)
                melody = []
                for i in range(len(melody_pattern)):
                    melody.append(notes[melody_pattern[i]])
                for j in range(len(measures)):
                    play_bass(measures[j], tonic*melody[j]+noise(1))
                play(3,tonic/2)

            def random_bass_thread():
                return Thread(target = random_bass)
            def random_song_walk(scale = s, tonic = note, measures_in_song = num_measures, beats = bpm, n_oct = 4):
                #print(tonic)    
                #print(scale)
                notes = octaves(scale, n_oct)
                notes = notes + [2**(n_oct)]
                measures = []
                for i in range(measures_in_song):
                    mes = measure(beats)
                    measures = measures + mes
                melody_pattern = random_walk_jump(len(measures), len(notes)-1)
                melody = []
                for i in range(len(melody_pattern)):
                    melody.append(notes[melody_pattern[i]])
                #play(1,main_tonic*2)
                for j in range(len(measures)):
                    play(measures[j], tonic*melody[j]+noise(1))
                play(2,tonic)
            def random_song_thread():
                return Thread(target = random_song_walk)
           
            
            
            random_bass_thread().start()
            random_song_thread().start()
            time.sleep(num_measures*bpm)
    finish = time.perf_counter()
    elapsed = finish - start
    print('Thank you for listening, this performance lasted  ' +   str(elapsed)  + '  seconds')


def just_tempered_synth(scales):
    """Plays a scale and tune in each key/scale combination    
       Input is a dict of scales"""
    print(colors.hide_cursor)
    print(screen + yellow)
    print('Hello, I am a program called the\n' + cyan + '       JUST_TEMPERED_SYNTHESIZER' + yellow + '\n I am an automatic music generator.' + '\n I do not know what music is,\n but I hope you enjoy mine.\nPardon its quality, I am only a machine.\n\n Current ' + green + 'key : ' + cyan + 'scale  =' )
    start = time.perf_counter()
    for scale_name, s in scales.items():
        for note_name , note in ordered_notes.items():
            print(' '*9 + green + note_name + '  : ' + cyan + scale_name, end = '\r')    
            def random_bass(scale = s, tonic = note,
                measures_in_song = num_measures, beats = bpm):
                notes = [1,1/2,2]
                if minor_third in scale: notes += [minor_third, minor_third/2]
                if major_third in scale: notes += [major_third, major_third/2]
                if perfect_fifth in scale: notes += [perfect_fifth, perfect_fifth/2]
                notes = sorted(notes)
                measures = []
                for i in range(measures_in_song):
                    mes = measure_bass(beats)
                    measures += mes
                melody_pattern = random_walk(len(measures), len(notes)-1)
                melody = []
                for i in range(len(melody_pattern)):
                    melody.append(notes[melody_pattern[i]])
                for j in range(len(measures)):
                    play_bass(measures[j], tonic*melody[j]+noise(1))
                play(3,tonic/2)

            def random_bass_thread():
                return Thread(target = random_bass)
            random_bass_thread().start()
            random_song_walk(scale = s, tonic = note)
    finish = time.perf_counter()
    elapsed = finish - start
    print('Thank you for listening, this performance lasted  ' +   str(elapsed)  + '  seconds')

def just_tempered_synth_with_scales(scales):
    """Plays a scale and tune in each key/scale combination
       Input is a dict of scales"""

    print(screen + yellow)
    print('Hello, I am a program called the\n' + cyan + '       JUST_TEMPERED_SYNTHESIZER' + yellow + '\n (as opposed to the Well-Tempered Clavier by JS Bach). I am a far more humble composer, but I can play in just intonation, and I can play fast, and I don\'t get tired (as long as you keep me plugged in!). I hope I can help you learn about different scales from around the world. You will hear a melody in{} scales in each key myself (the program). I hope you enjoy. '.format(len(scales)) )
    temp = input('      Press ENTER to begin:')
    start = time.perf_counter()
    for note_name , note in ordered_notes.items():   
        for scale_name, s in scales.items():
            print(' '*8 + green + note_name + '  :  ' + cyan + scale_name)    
            multi_octave_scale(s, 3, tonic = note)
            print(yellow + 'Now hear a melody I came up with:\nPardon its quality, I am only a machine')
            def random_bass(scale = s, tonic = note,
                measures_in_song = num_measures, beats = bpm):
                notes = [1,1/2,2]
                if minor_third in scale: notes += [minor_third, minor_third/2]
                if major_third in scale: notes += [major_third, major_third/2]
                if perfect_fifth in scale: notes += [perfect_fifth, perfect_fifth/2]
                notes = sorted(notes)
                measures = []
                for i in range(measures_in_song):
                    mes = measure_bass(beats)
                    measures = measures + mes
                melody_pattern = random_walk(len(measures), len(notes)-1)
                melody = []
                for i in range(len(melody_pattern)):
                    melody.append(notes[melody_pattern[i]])
                play(1,tonic/2)
                for j in range(len(measures)):
                    play(measures[j], tonic*melody[j]+noise(1))
                play(3,tonic/2)

            def random_bass_thread():
                return Thread(target = random_bass)
            random_bass_thread().start()
            random_song_walk(scale = s, tonic = note)
    finish = time.perf_counter()
    elapsed = finish - start
    print('Thank you for listening, this performance lasted  ' +   str(elapsed)  + '  seconds')

just_tempered_synth(pentatonic_scales)
