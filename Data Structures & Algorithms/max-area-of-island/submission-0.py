class Solution:
    # Time: O(n*m)
    # Space: O(n*m)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        maxArea = 0

        visited = set()
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= ROW or j >= COL:
                return 0
            if (i,j) in visited or grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
            up = dfs(i+1, j) 
            down = dfs(i-1, j) 
            left = dfs(i, j-1)
            right = dfs(i, j+1)

            return 1 + up + down + left + right
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                maxArea = max(maxArea, dfs(i, j))
        
        return maxArea