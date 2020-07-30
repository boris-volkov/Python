from itertools import *

def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end = ' ')
    print('\n')

print('unique combos:\n')
show(combinations('abcdefgh', r=4))
print('combinations with replacement:\n')
show(combinations_with_replacement('abcdefgh', r=3))
