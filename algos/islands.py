class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        # collect all points bound by the equivalence relation
        
        # go through and check equality 
        # build the equivalence classes
        equiv_classes = []

        
        # need to make an equations generator to feed into here. 
        def grid_generator(grid):
            return ( (i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '1')
        
        def list_neighbors(grid, point):
            i = point[0]
            j = point[1]
            neighbors = [(i,j)]
            if i < len(grid) - 1:
                if grid[i+1][j] == '1':
                    neighbors.append((i+1,j))
            if j < len(grid[0]) - 1:
                if grid[i][j+1] == '1':
                    neighbors.append((i,j+1))
            if i > 0:
                if grid[i-1][j] == '1':
                    neighbors.append((i-1,j))
            if j > 0:
                if grid[i][j-1] == '1':
                    neighbors.append((i,j-1))
            return neighbors
        
        gen = grid_generator(grid)
        for point in gen:
            equiv_class = list_neighbors(grid, point)
            print(equiv_class)
            self.insert(equiv_classes, *equiv_class)
        

        print('final classes', equiv_classes)

        #if there are links between different classes, they must be joined.

        to_delete = set()
        for i in range(len(equiv_classes) - 1):
            for j in range(i + 1, len(equiv_classes)):
                if not set.isdisjoint(equiv_classes[i], equiv_classes[j]):
                        print('updating classes', equiv_classes[j], equiv_classes[i],i,j)
                        equiv_classes[j].update(equiv_classes[i])
                        to_delete.add(i)
                        print('going to delete', i)
        for i in reversed(sorted(list(to_delete))):
            print('popping', i)
            equiv_classes.pop(i)
            

        print('final classes, after joining', equiv_classes)
        
        return len(equiv_classes)

    @staticmethod
    def insert(lis, *items): # star passes to star
        for cl in lis:
            print()
            print('checking membership', items, cl)
            print([a in cl for a in items])
            if any([a in cl for a in items]):
                for b in items:
                    print('inserting', b, 'into', cl)
                    cl.add(b)
                return    
        lis.append({*items})


tester = Solution()
case = [["1","1","1","1","1","1","1","1","1"],["1","0","0","0","0","0","0","0","1"],["1","0","1","0","1","0","1","0","1"],["1","0","1","1","1","1","1","0","1"],["1","0","1","0","1","0","1","0","1"],["1","0","0","0","0","0","0","0","1"],["1","1","1","1","1","1","1","1","1"]]
for line in case:
    print(line)
tester.numIslands(case)
