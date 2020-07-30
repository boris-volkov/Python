from collections import defaultdict

def groupThePeople(groupSizes):
    sets = []

    D = defaultdict(list)

    for i, n in enumerate(groupSizes):
        D[n] += [i]

    for i, lis in D.items():
        this_group = []
        while lis:
            for _ in range(i):
                this_group.append(lis.pop())
            sets.append(this_group)
            this_group = []
    return sets

test = [3,3,3,3,3,1,3]
print(groupThePeople(test))
    
        
