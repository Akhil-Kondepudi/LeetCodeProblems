class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        width, height = len(grid[0]), len(grid)
        marked = [[False]* width for x in range(height)]
        
        def helper(x,y):
            if x < 0 or x >= height or y < 0 or y >= width:
                return False
            elif grid[x][y] == "0":
                return False
            elif marked[x][y]:
                return False
            else:
                marked[x][y] = True
                helper(x + 1, y)
                helper(x - 1, y)
                helper(x, y + 1)
                helper(x, y - 1)
                return True
                
        
        out = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if helper(x, y):
                    out += 1
        return out
        
        