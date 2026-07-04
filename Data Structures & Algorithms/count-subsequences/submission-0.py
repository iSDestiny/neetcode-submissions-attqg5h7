# Recursion Decision:
# - base cases:
#   - if i == len(s) and j == len(t): return 1 (We have a valid subsequence equal to t)
#   - if i == len(s): return 0 (This means that we processed all of s but didn't get a match to t with the current subsequence)
# - Include current index i of s in subsequence if equal to t[j]
#   -> advance i and j (index of t): fn(i+1, j+1)
# - Exclude index i of s:
#   -> advance i: fn(i+1, j)
#
# Brute Force:
#   Time: O(2^n)
#   Space: O(n)
# Memoization:
#   Time: O(n*m) where n is len of s and m is len of t
#   Space: O(n*m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = [[-1] * len(t) for _ in range(len(s))]

        def recurse(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if cache[i][j] > -1:
                return cache[i][j]
            total = recurse(i+1, j)
            if s[i] == t[j]:
                total += recurse(i+1,j+1)
            cache[i][j] = total
            return cache[i][j]
        
        return recurse(0,0)
        