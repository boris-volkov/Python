from getch import getch
import colors
from sounds import *

print(colors.hide_cursor)

tonic = C
scale = major_scale
for i in range(len(scale)):
    scale[i]*=tonic


alphabet = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWWWXYYZ"]

alphabet.extend("now I know my A B C's next time won't you sing with me?".split(' '))

melody = [ 
           (.25, scale[0]), (.25, scale[0]),
           (.25, scale[4]), (.25, scale[4]),
           (.25, scale[5]), (.25, scale[5]),
           (.5, scale[4]),

           (.25, scale[3]), (.25, scale[3]),
           (.25, scale[2]), (.25, scale[2]),
           (.125, scale[1]), (.125, scale[1]),
           (.125, scale[1]), (.125, scale[1]),
           (.5, scale[0]), #p
           
           (.25, scale[4]), (.25, scale[4]),
           (.25, scale[3]), 
           (.25, scale[2]),(.25, scale[2]),
           (.5, scale[1]),
           
           (.125, scale[4]), #w
           (.125, scale[4]), #w
           (.125, scale[4]), #w
           
           (.25, scale[3]),
           (.25, scale[2]),
           (.25, scale[2]),
           (.5, scale[1]),
           (.25, scale[0]),
           (.25, scale[0]),
           (.25, scale[4]),
           (.25, scale[4]),
           (.25, scale[5]),
           (.25, scale[5]),
           (.25, scale[4]),
           (.25, scale[3]),
           (.25, scale[3]),
           (.25, scale[2]),
           (.25, scale[2]),
           (.25, scale[1]),
           (.25, scale[1]),
           (1, scale[0])
           ]

while 1:
    i = 0
    while i < len(melody):
        getch()
        print(colors.clear_screen)
        print(alphabet[i].center(6), end='\r')
        play_pluck(*melody[i])
        i += 1






