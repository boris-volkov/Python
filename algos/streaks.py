import collections

class Solution:
    def isPossibleDivide(self, nums, k):
        if not nums: return True
        if len(nums)%k != 0: return False
        
        c = collections.Counter(nums)
        while c:
            cur = min(c)
            count = c[cur]
            for i in range(k):
                if c[cur+i] == count:
                    c.pop(cur+i)
                    continue
                else:
                    c[cur+i] -= count                
                if c[cur+i] < 0:
                    return False
        return True  
