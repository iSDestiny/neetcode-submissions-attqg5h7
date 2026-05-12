class Solution:
    # Time: O(n*m)
    # Space: O(max(n, m)) recursion depth
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        count = 0
        visited = set()
        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= ROW or j >= COL:
                return
            if (i,j) in visited or grid[i][j] == "0":
                return

            visited.add((i, j))
            # vertical
            dfs(i+1, j)
            dfs(i-1, j)
            # horizontal
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "0" or (i, j) in visited:
                    continue
                dfs(i, j)
                count += 1
        return count
