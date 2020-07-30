"""
Program will compare different ways to use queues
"""

import collections
import random
import time

data = random.sample(range(10**6), k = 10**6)

def tester(times):
    c = collections.deque()
    start = time.perf_counter()
    for _ in range(times):
        c.append(random.choice(data))

    for _ in range(times):
        if random.random() < 0.5:
            c.popleft() 
        else:
            c.append(random.choice(data))
    elapsed = time.perf_counter() - start
    print(elapsed)

