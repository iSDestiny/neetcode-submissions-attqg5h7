class Solution:
    # Time: O(2^m*2^n) = O(2^(m+n)) O(m*n)
    # Space: O(m+n)
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1]*n for _ in range(m)]
        def recurse(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if cache[i][j] > -1:
                return cache[i][j]
            cache[i][j] = recurse(i+1, j) + recurse(i,j+1)
            return cache[i][j]
        return recurse(0,0)