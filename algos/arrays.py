

def apply_permutation(perm, A):
#the second part of this method just sorts the permutation array.
#same idea that goes with the breaking of a permutation into 2-cycles
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]

def next_permutation(perm):
    #changes the array passed in, does not return a copy!
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 
            and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return [] #perm is the last permutation.

    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm

def biggest_sub(array):
    start_index = running_sum = 0
    max_so_far = (0,0,0) 
        #interpreted as (max subarray sum, start index, end index)
    for i,val in enumerate(array):

        if running_sum > 0:
            running_sum += val
        else:
            running_sum = val
            start_index = i
        
        if running_sum > max_so_far[0]:
                max_so_far = (running_sum, start_index, i+1)
    return max_so_far 
