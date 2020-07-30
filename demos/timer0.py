import time
def timer(func, *args):
    start = time.clock() # only good for windows
    for i in range(1000):
        func(*args)
    return time.clock() - start

# bad timer function!
# charges the cost of range to
# the function being tested,
# doesns't tell if func worked
# gives total time which might
# be wrong if computer is overloaded


