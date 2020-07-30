def longestCommonSubsequence_O(text1, text2):    
    # to weed out all of the mismatches right away
    matches = set.intersection(set(text1), set(text2))
    collection1 = [letter for letter in text1 if letter in matches]
    collection2 = [letter for letter in text2 if letter in matches]
    
    dp_array = [0]*(len(collection2) + 1)
    
    for i, item1 in enumerate(collection1):  
        memory_bit = 0
        for j, item2 in enumerate(collection2, 1):
            cur_val = dp_array[j]
            if item1 == item2:
                dp_array[j] = memory_bit + 1
            else:
                dp_array[j] = max(dp_array[j], dp_array[j-1])
            memory_bit = cur_val
        
    return dp_array[-1]


def longestCommonSubsequence(collection1, collection2):

    dp_array = [0]*(len(collection2) + 1)
    for i, item1 in enumerate(collection1):
        memory_bit = 0
        for j, item2 in enumerate(collection2, 1):
            cur_val = dp_array[j]
            if item1 == item2:
                dp_array[j] = memory_bit + 1
            else:
                dp_array[j] = max(dp_array[j], dp_array[j-1])
            memory_bit = cur_val

    return dp_array[-1]

if __name__ == '__main__':
    import time

    collection1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    collection2 = ['m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    start_time = time.perf_counter()
    for _ in range(100000):
        longestCommonSubsequence(collection1, collection2)
    print('non-optimized finished in', time.perf_counter() - start_time)

    start_time = time.perf_counter()
    for _ in range(100000):
        longestCommonSubsequence_O(collection1, collection2)
    print('optimized finished in', time.perf_counter() - start_time)

    #run 
    '''
    non-optimized finished in 5.617266239001765
    optimized finished in 0.3257247389992699
    '''

