    def triangle_sum(t):
        if len(t) == 1:
            return t[0][0]

        costs = [None for _ in range(len(t))]
        costs[0] = t[0][0] + t[1][0]
        costs[1] = t[0][0] + t[1][1]

        for i in range(2, len(t)):
            this_min = costs[0]
            for j in range(i):
                try:
                    next_min = min(costs[j], costs[j+1])
                except:
                    last = costs[j-1]
                costs[j] = triangle[i][j] + this_min
                this_min = next_min
            costs[i] = triangle[i][i] + last
            
        return min(costs)    


triangle = [ [2] , [3,4] , [6,5,7] , [4,1,8,3] ]
print(triangle_sum(triangle))


"""

        if not triangle:
            return

        top = triangle[0][0]
        if len(triangle) == 1:
            return top

        old = [top + i for i in triangle[1]]

        for i in range(2, len(triangle)):

            new = [old[0] + triangle[i][0]]
            for j in range(1, i):
                new.append( triangle[i][j] + min(old[j-1], old[j]) )
            new.append(old[-1] + triangle[i][-1])
            old = new

        return min(old)
"""
