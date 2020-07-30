class num_found(Exception):
    def __init__(self, depth):
        self.depth = depth

class Solution:            
    def brokenCalc(self, x: int, y: int) -> int:
        if y <= x:
            return x-y
        visited = set()
        
        try:
            bfs(visited x, y, 0)
        except num_found as x:
            return x.depth
        else:
            return
                
def bfs(visited, num, target, depth):
    que = [(num, 0)]
    depth = 0
    while que:     
        nex = que.pop(0)
        num = nex[0]
        depth = nex[1]
        
        if num == target: raise num_found(depth)
        
        if num > 0 and (num-1) not in visited:
            visited.add(num - 1)
            que.append((num-1, depth + 1))
            
        if num < (target*2) and num*2 not in visited:
            visited.add(num*2)
            que.append((num*2, depth + 1))
        

        
