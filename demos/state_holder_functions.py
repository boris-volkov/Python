def add_count(x):
    count = x
    def inner(y):
        nonlocal count
        print(y+1, count)
        count += 1
    return inner

def sub_count(x):
    def inner(x):
        inner.count += 1         # knows its own name
        print(x-1, inner.count)
    inner.count = 0             
    return inner
