class Solution:
    def equationsPossible(self, equations):
        equiv_classes = []
        
        for eq in equations:
            if eq[1] == '=':
                print(equiv_classes)
                if eq[0] == eq[-1]: pass
                else:
                    self.insert(eq[0], eq[-1], equiv_classes)
        print('final classes', equiv_classes) 

        #if there are links between different classes, the must be joined.

        to_delete = []
        for i in range(len(equiv_classes) - 1):
            for j in range(i + 1, len(equiv_classes)):
                if not set.isdisjoint(equiv_classes[i], equiv_classes[j]):
                        equiv_classes[j].update(equiv_classes[i])
                        to_delete.append(i)
        for i in reversed(sorted(to_delete)):
            equiv_classes.pop(i)
        
        print('final classes, after joining', equiv_classes) 

        for eq in equations:
            if eq[1] == '!':
                print('checking enemies', eq[0], eq[-1])
                if eq[0] == eq[-1]: return False
                if self.check_enemies(eq[0], eq[-1], equiv_classes): return False

        for i in range(len(equiv_classes) - 1):
            for j in range(i + 1, len(equiv_classes)):
                print('checking disjoint: ', equiv_classes[i], equiv_classes[j],i,j)
                if not set.isdisjoint(equiv_classes[i],equiv_classes[j]): return False
                
        return True

    @staticmethod 
    def insert(a,b, lis):
        for cl in lis:
            if a in cl or b in cl:
                cl.add(a)
                cl.add(b)
                return
        lis.append(set([a,b])) 
        
    @staticmethod
    def check_enemies(a,b,lis):
        for cl in lis:
            if a in cl and b in cl:
                return 1
        return 0



test = Solution()
case1 = ["a==b","e==c","b==c","a!=e"]
case2 = ["b==d","c==a","h==a","d==d","a==b","h!=k","i==h"]
print(test.equationsPossible(case1))
print(test.equationsPossible(case4))
