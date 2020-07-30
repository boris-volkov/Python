import time
import colors

def timer(func):
    def inner(*args, **kwargs):
        begin = time.perf_counter()
        factors = func(*args,**kwargs)
        end = time.perf_counter()
        runtime = end - begin
        print(colors.cyan + 'took ' + str(runtime) + ' seconds' + colors.yellow)
        return factors
    return inner

def prime_fac(x):
    factors = []
    num = x
    while num > 1:
        for i in range(2,num+1):
            if num%i == 0:
                num = num // i
                factors.append(i)
                break
    return factors           

@timer
def factors(x):
    prime_facts = prime_fac(x)
    factors = set()
    for i in range(1,2**len(prime_facts)):
        indexer = i
        factor = 1
        j = 0
        while indexer:
            if indexer&1:
                factor *= prime_facts[j]
            indexer >>= 1
            j += 1
        factors.add(factor)
    factors.add(1)
    print(colors.red + str(len(factors)) + ' factors' + colors.yellow)
    return sorted(factors)

@timer
def brute_force_fac(x):
    factors = []
    for i in range(1,x//2 + 1):
        if x%i == 0:
            factors.append(i)
    factors.append(x)
    return factors
