import speech_recognition as sr
import pocketsphinx as spx
import time
import sys

print('\u001b[96m')

localtime = time.asctime( time.localtime(time.time()) )

r = sr.Recognizer()

mic = sr.Microphone()

recordings = []

with mic as source:
    r.adjust_for_ambient_noise(source)


while True:
    try:
        with mic as source:
            audio = r.listen(source, phrase_time_limit = 2)
        Isaid = r.recognize_google(audio)
        print(Isaid)
        recordings.append(Isaid)
    except KeyboardInterrupt:
        break
    except:
        pass

with open(localtime + '_recording.txt', 'a+') as target_file:
    for i in range(len(recordings)):
        target_file.write(recordings[i] + '\n')

#def callback(r, audio):
#    try:
#        print("The Sphinx thinks you said " + r.recognize_sphinx(audio))
#    except:
#        pass
#
#with mic as source:
#    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
#
#stop_listening = r.listen_in_background(mic, callback)
## `stop_listening` is now a function that, when called, stops background listening
#
## do some unrelated computations for 5 seconds
##for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
#
## calling this function requests that the background listener stop listening
##stop_listening(wait_for_stop=False)
