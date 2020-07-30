# usage examples: for   P(x) = x³ - 7x + 6      :  call  rational_zeros([1,0,-7,6])
#                 for   P(x) = -3x³ - 3x² + 18x :  call  rational_zeros([-3,-3,18,0])


from fractions import Fraction
import math

# returns a prime factorization of a natural number 
def prime_factors(x):
    if x == 1 : return []
    factors = []
    num = x
    for i in range(2,num+1):
        while num%i == 0:
            num = num // i
            factors.append(i)        
        if num == 1: return factors

# returns full set of factors of a natural number
def factors(x):
    prime_facs = prime_factors(x)
    factors = set()
    factors.add(1)
    for i in range(1,2**len(prime_facs)):
        indexer = i
        factor = 1
        j = 0
        while indexer:
            if indexer&1:
                factor *= prime_facs[j]
            indexer >>= 1
            j += 1
        factors.add(factor)
    return sorted(factors)

# synthetic division
def is_zero(P,x):     
    polynomial = list(reversed(P))
    remainder = polynomial.pop()
    while polynomial:
        remainder = x*remainder + polynomial.pop()
    return math.isclose(remainder,  0)

# rational root theorem
def possible_zeros(P):
    numerators = factors(abs(P[-1]))
    denominators = factors(abs(P[0]))
    candidates = set()
    for n in numerators:
        for d in denominators:
            candidates.add(Fraction(n,d))
            candidates.add(Fraction(-n,d))
    return candidates

# polynomial factor theorem
def rational_zeros(P):
    zeros = set()
    while P[-1] == 0:
        zeros.add(0)
        P.pop()
    candidates = list(possible_zeros(P))
    for c in candidates:
        if is_zero(P,c):
            zeros.add(c)
    return zeros

if __name__ == '__main__':
    import sys
    coeffs = [int(c) for c in sys.argv[1:]]
    print(rational_zeros(coeffs))
