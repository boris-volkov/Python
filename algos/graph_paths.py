"""
A general purpose graph traverser class

"""

class Node(object):
    def __init__(self, label, extra=None):
        self.name = label
        self.data = extra
        self.arcs = []

    def __repr__(self):
        return self.name

    def search(self, goal):
        Graph.paths = []
        self.generate([self], goal)
        Graph.paths.sort(key=lambda x: len(x))
        return Graph.paths

    def generate(self, path, goal):
        if self == goal:
            Graph.paths.append(path)
        else:
            for arc in self.arcs:
                if arc not in path:
                    arc.generate(path + [arc], goal)


if __name__ == '__main__':
    for name in 'ABCDEFG':
        exec("%s = Graph('%s')" % (name, name))

    A.arcs = [B, E, G]
    B.arcs = [C]
    C.arcs = [D, E]
    D.arcs = [F]
    E.arcs = [C, F, G]
    G.arcs = [A]

    A.search(G)
    for (start, stop) in [(E,D), (A,G), (G,F)]:
        print(start.search(stop))

