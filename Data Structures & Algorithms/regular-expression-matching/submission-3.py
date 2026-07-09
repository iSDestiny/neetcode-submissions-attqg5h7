# base case:
# - i == len(s): return j == len(p)
# - s[i] != p[j]: return False
# 
# 3 non base cases:
# - s[i] == p[j] or p[j] == ".": recurse(i+1, j+1)
# - p[j] == "*": 
#    - if s[i] == p[j-1]: return recurse(i+1, j) or recurse(i+1, j+1)
# Brute Force:
#   Time: O(2^m+n)
#   Space: O(n+m)
# Memoization:
#   Time: O(m*n)
#   Space: O(m*n)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        cache = [[None]*(m+1) for _ in range((n+1))]

        def recurse(i: int, j: int) -> int:
            if j == m:
                return i == n
            if cache[i][j] != None:
                return cache[i][j]
            
            if j+1 < m and p[j+1] == "*":
                cache[i][j] = recurse(i, j+2)
                if i < n and (s[i] == p[j] or p[j] == ".") and recurse(i+1, j):
                    cache[i][j] = True
            elif i < n and (s[i] == p[j] or p[j] == "."):
                cache[i][j] = recurse(i+1, j+1)
            
            if cache[i][j]:
                return True
                
            return False
        
        return recurse(0,0)