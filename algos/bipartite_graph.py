from collections import defaultdict
import collections

class OddFound(Exception): pass

class Solution0(object):
    """
    Alternate definition of bipartite:
    graph with no odd cycles. This rather
    slow algorithm must check every cycle
    and raise an exception as soon as it
    finds an odd one (which might be a very
    long time in a large bipartite graph)
    """
    def isBipartite(self, graph):
        if not graph: return True
        try:
            for i in range(len(graph)):
                Solution0.find_cycles(i, graph)
        except OddFound:
            return False
        else:
            return True
        
    def find_cycles(me, graph):
        paths = []
        for arc in graph[me]:
                paths = [arc], paths
        
        while paths:
            front, paths = paths
            current = front[-1]
            if current == me:
                if len(front) % 2 == 1:
                    raise OddFound()            # means an odd cycle was found
            
            else: 
                for i in graph[current]:
                    if i not in front:
                        paths = front + [i], paths    


class Solution1(object):
    def isBipartite(self, graph):
        color = defaultdict(lambda: -1)
        return all(self.dfs(graph, v, edges, 0, color) for v, edges in enumerate(graph) if color[v] == -1)

    def dfs(self, graph, v, edges, cur_color, color):
        if color[v] != -1: return color[v] == cur_color
        color[v] = cur_color
        return all(self.dfs(graph, e, graph[e], int(not cur_color), color) for e in edges)


class Solution2(object):
    def isBipartite(self, graph):
        def dfs(v, cur_color):
            if v in color:
                return color[v] == cur_color
            color[v] = cur_color
            return all(dfs(w, cur_color ^ 1) for w in graph[v])
        color = {}
        return all(dfs(v, 0) for v in range(len(graph)) if v not in color)
    

"""
    1st approach: BFS + nodes coloring

    Time    O(V+E)
    Space   O(V+E)
    156 ms, faster than 62.09%
"""


class Solution3(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, seen) == False:
                    return False
        return True

    def check(self, graph, start, seen):
        q = [(start, 1)]
        while len(q) > 0:
            pop, color = q.pop(0)
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue
            seen[pop] = color
            vertices = graph[pop]
            for v in vertices:
                q.append((v, -color))
        return True


"""
    2nd approach: recursive DFS + nodes coloring

    Time    O(V+E)
    Space   O(V+E)
    164 ms, faster than 40.67%
"""


class Solution4(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, 1, seen) == False:
                    return False
        return True

    def check(self, graph, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = graph[node]
        for v in vertices:
            if self.check(graph, v, -color, seen) == False:
                return False
        return True

class Solution5(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        party = [set(), set()]

        for node in range(len(graph)):
            if node not in party[0] and node not in party[1]:
                queue = collections.deque([(node, 0)])
                while queue:
                    node, p = queue.popleft()
                    for nei in graph[node]:
                        if nei in party[p]:
                            return False
                        elif nei not in party[1-p]:
                            party[1-p].add(nei)
                            queue.append((nei, 1-p))
        return True

if __name__ == '__main__':

    import random

    def random_graph(n):
        """
        Makes random graph with n nodes 
        """

        graph = [[] for _ in range(n)]
        for i in range(random.randint(1, 1000)): # random number of nodes as well
            connect = random.sample(range(n), 2)
            if connect[0] not in graph[connect[1]]:
                graph[connect[0]].append(connect[1])
                graph[connect[1]].append(connect[0])

        return graph

    def random_bipartite(n):
        graph = [[] for _ in range(n)]
        blues = set(random.sample(range(n), random.randint(0,n)))
        reds = set.difference(set(range(n)), blues)
        
        for b in blues:
            graph[b].extend(list(random.sample(reds, random.randint(0,len(reds)))))
            for r in graph[b]:
                graph[r].append(b)
        return graph
                


    zero  = Solution0()
    one   = Solution1()
    two   = Solution2()
    three = Solution3()
    four  = Solution4()
    five  = Solution5()

    funcs = [x.isBipartite for x in [one, two, three, four, five] ]
    import time
    test_graphs      = [random_graph(100) for _ in range(200)]
    bipartite_graphs = [random_bipartite(100) for _ in range(2000)]
    for f in funcs:
        start = time.perf_counter()
        for graph in test_graphs:
            f(graph)
        for graph in bipartite_graphs:
            if f(graph) == False : print('broken')

            
        finish = time.perf_counter() - start
        print(f.__self__, finish)


    """
    prints:
    <__main__.Solution1 object at 0x7fa32dfd3198> 1.9808858780015726
    <__main__.Solution2 object at 0x7fa32dfd32b0> 1.0709960170024715
    <__main__.Solution3 object at 0x7fa32dfd32e8> 2.7216683789993112
    <__main__.Solution4 object at 0x7fa32dfd3320> 0.7989234300002863
    <__main__.Solution5 object at 0x7fa32dfd3358> 0.35835606799810193

    """
