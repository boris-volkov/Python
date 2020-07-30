import numpy
import functools

def integral(fun, a, b, inc):
    r = numpy.arange(a,b,inc)
    return functools.reduce(lambda x,y : x + fun(y)*inc , r, 0)




