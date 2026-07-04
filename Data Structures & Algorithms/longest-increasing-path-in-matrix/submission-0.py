class Solution:
    # Perform a DFS from every cell (row,col) to get the longest strictly increasing path from this cell
    # For every cell store the score in a cache to be used for later computation (memoization)
    # Time: O(n*m)
    # Space: O(n*m)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        cache = [[-1]*COL for _ in range(ROW)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            directions = [(1, 0), (-1, 0), (0, -1), (0,1)]
            maxLen = 1
            for dr, dc in directions:
                r2,c2 = r+dr, c+dc
                if r2 < 0 or c2 < 0 or r2 >= ROW or c2 >= COL:
                    continue
                if matrix[r2][c2] > matrix[r][c]:
                    maxLen = max(maxLen, 1+dfs(r2,c2))
            cache[r][c] = maxLen
            return cache[r][c]
        
        maxLen = 1
        for r in range(ROW):
            for c in range(COL):
                maxLen = max(maxLen, dfs(r,c))
        return maxLen
        