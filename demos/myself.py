x = 0

def f():
    global x
    x += 1

def g():
    import myself
    myself.x += 1

def h():
    import sys
    me = sys.modules[__name__]
    me.x += 1

f();    print('after f  :', x) 
g();    print('after g  :', x)
h();    print('after h  :', x)


# note the name of the file #
