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
        Isaid = r.recognize_sphinx(audio)
        print(Isaid)
        recordings.append(Isaid)
    except KeyboardInterrupt:
        break
    except:
        pass

with open(localtime + '_recording.txt', 'a+') as target_file:
    for i in range(len(recordings)):
        target_file.write(recordings[i] + '\n')
