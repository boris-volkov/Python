import time

def test():
    count = 0
    start = time.time()
    finish = start + 10
    now = start
    while (now < finish):    
        count += 1
        print(count)
        _ = input()
        now = time.time()
    print(str(count/10))
