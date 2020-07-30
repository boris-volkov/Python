def nthUglyNumber(self, n):
    ugly = [1]
    # indeces of numbers to be multiplied
    # by 2, 3, and 5
    i2 = i3 = i5 = 0 
    while len(ugly) < n:
        # push them forward if this number doesn't
        # need to be multiplied any more by that num
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        # append the smallest of the numbers that
        # are still greater than the biggest ugly so far
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]


