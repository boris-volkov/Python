def roman_to_integer(s):
    T = {'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}

    return functools.reduce(
            lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
            reversed(range(len(s) - 1)), T[s[-1]])


'''
functools.reduce(function, iterable[,initializer])

apply function of two arguments cumulatively to items of sequence,
left to right, reducing sequence to a single value

ex: 

'''
