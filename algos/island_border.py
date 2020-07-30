class Solution:
    def colorBorder(self, grid, i, j, color):
        photo = [bytearray(len(grid[0])) for _ in range(len(grid))]

        landed_color = grid[i][j]
        print(landed_color)
        dfs(photo, grid, i, j, landed_color)
        
        for row in photo:
            print(row)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if photo[i][j] > 1:
                    grid[i][j] = color

        return grid

def dfs(photo, grid, i, j, color):
    if 0 > i or i >= len(grid):      return
    if 0 > j or i >= len(grid[0]):   return
    if grid[i][j] != color:          return 
    if photo[i][j]:                  return

    photo[i][j] += 1            # visited squares will = 1
    if on_border(grid, i, j):   # border squares will = 2
        photo[i][j] += 1

    dfs(photo, grid, i, j+1, color)
    dfs(photo, grid, i+1, j, color)
    dfs(photo, grid, i, j-1, color)
    dfs(photo, grid, i-1, j, color)

def on_border(grid, i, j):
    try:
        if grid[i][j] != grid[i][j+1]: return True
        if grid[i][j] != grid[i+1][j]: return True
        if grid[i][j] != grid[i][j-1]: return True
        if grid[i][j] != grid[i-1][j]: return True
    except IndexError:
        return True         # means hit the edge

if __name__ == "__main__":
    sol = Solution()

    grid = [[1,1,1],[0,1,0],[0,1,1]]
    for row in grid: 
        print(row)
    print()
    for row in sol.colorBorder(grid, 1, 0, 7):
        print(row)
