import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph: return 
        Solution.safe = []
        Solution.unsafe = set()
        for i in range(len(graph)):
            if i in Solution.unsafe: pass
            if any(n in Solution.unsafe for n in graph[i]):
                Solution.unsafe.add(i)
            else:
                if Solution.check(i, graph):
                    Solution.safe.append(i)
                
        return Solution.safe
                
    @staticmethod            
    def check(node, graph):
        paths = collections.deque()
        paths.append([node])
        state = True
        while paths:
            front = paths.pop()
            curr = front[-1]
            
            for node in graph[curr]:
                if node in front or node in Solution.unsafe:
                    Solution.unsafe.update(front) # update with everything on the bad path!
                    state = False
                else:
                    paths.append(front + [node])
        return state
