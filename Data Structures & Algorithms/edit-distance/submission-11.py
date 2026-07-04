# Brute Force Recursion:
# - base cases:
#   - if j == len(word2): return len(word1) - i # If word2 is done but word1 isn't, then delete the rest of word1
#   - if i == len(word1): return len(word2) - j # If word1 is done but word2 isn't, then insert the rest of missing chars
# - if word1[i] == word2[j]: recurse(i+1, j+1)
# - else:
#   - Insert: recurse(i, j+1)
#   - Delete: recurse(i+1, j)
#   - Replace: recurse(i+1, j+1)
# Time: O(3^n+m)
# Space: O(n+m)
#
# Memoization:
# Time: O(n*m)
# Space: O(n*m)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[-1]*len(word2) for _ in range(len(word1))]

        def recurse(i: int, j: int) -> int:
            if j == len(word2): 
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if cache[i][j] > -1:
                return cache[i][j]
            # match
            if word1[i] == word2[j]:
                cache[i][j] = recurse(i+1,j+1)
                return cache[i][j]
            insert = recurse(i, j+1) 
            delete = recurse(i+1, j)
            replace = recurse(i+1, j+1)

            cache[i][j] = 1 + min(insert, delete, replace) 
            return cache[i][j]
        
        return recurse(0,0)