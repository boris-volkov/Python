import itertools, collections

def atoi(word, mapping):
    n = 0
    for letter in word:
        n *= 10
        n += mapping[letter]
    return n
    
def mapping(n):                
    return itertools.permutations(range(0,10), n)
    
def isSolvable(words, result):
    letter_set = set()
    lasts = []
    firsts = set()
    for word in words + [result]:
        lasts.append(word[-1])
        firsts.add(word[0])
        for letter in word:
            letter_set.add(letter)
    letter_set = list(letter_set)
    
    gen = mapping(len(letter_set))
    lasts.pop()
    try:
        while 1:
            dictionary = {}
            x = next(gen)
            for i, l in enumerate(letter_set):
                dictionary[l] = x[i]
            if any(dictionary[l] == 0 for l in firsts):
                continue
            if (((sum(dictionary[l] for l in lasts))%10)!=dictionary[result[-1]]):
                continue
            if check(words, result, dictionary) : print(dictionary)
    except StopIteration:
        return False
            
def check(words, result, mapping):
    return sum(atoi(word, mapping) for word in words) == atoi(result, mapping)

            
if __name__ == '__main__':
    import sys


