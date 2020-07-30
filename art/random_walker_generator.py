from random import random

def random_walker():
    while 1:
        r = random()
        if r < .5:
            yield 1
        else:
            yield -1

def walker():
    return (1 if random() < 5 else -1)
