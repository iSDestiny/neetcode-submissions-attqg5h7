class Solution:
    # Brute Force:
    # Time: O(2^(n+m))
    # Space: O(m+n)
    # Memoization:
    # Time: O(n*m)
    # Space: O(n*m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        cache = [[-1]*m for _ in range(n)] 
        def recurse(i: int, j: int) -> int:
            if i >= n or j >= m:
                return 0
            if cache[i][j] > -1:
                return cache[i][j]
            if text1[i] == text2[j]:
                cache[i][j] = 1 + recurse(i+1, j+1)
                return cache[i][j]
            cache[i][j] = max(recurse(i+1, j), recurse(i, j+1))
            return cache[i][j]
        return recurse(0,0)