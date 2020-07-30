def permute_rec(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute_rec(rest):
                res.append(x + seq[i:i+1])
    return res

def permute_gen(seq):
    # generator does the same thing but mimimizes
    # memory usage and delay for results
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[ :i] + seq[i+1: ]
            for x in permute_gen(rest):
                yield seq[i:i+1] + x
