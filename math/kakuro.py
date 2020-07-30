from itertools import combinations
import sys

if __name__ == '__main__':
    target = int(sys.argv[1])
    num = int(sys.argv[2])
    for comb in combinations(range(1,10), num):
        if sum(comb) == target:
            print(comb)
