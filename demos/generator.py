# these functions are compiled specially as generators
# built to return objects with iteration protocol methods
# when called they return a generator object that supports
# the iteration interface
# it doesn't spit out all the values at once like range()
# but gives them up and goes into state suspension until
# the next call.
# the function, along with its namespace is frozen in time.
# generator functions can be better in terms of memory and performance
# the save functions from having to do all the work up front

def factor_generator(x):
    return (i for i in range(1,x+1) if x%i == 0)

def factor_generator_2(x):  #these functions do the same thing
    for i in range(1, x+1):
        if x%i == 0:
            yield i

f = factor_generator(12)
g = factor_generator_2(12)
print(next(factor_generator(12)))
print(next(factor_generator(12)),next(factor_generator(12)))
# running next on the function keeps returning the first element
# need to actually create a generator object 
print('type of f:')
print(type(f))

n = next(f)
l = list(f)
s = set(f)
ss = set(g)

print('list:')
print(l)
print('set:')
print('generator is already exhausted, has hit StopIteration')
print(s)
print('set from other generator:')
print(ss)
print('generators are their own iterators:')
print('iter(f) is f? : ', iter(f) is f)

print(sum(factor_generator(12)))
print(sum(i for i in range(1,13) if 12%i == 0))
