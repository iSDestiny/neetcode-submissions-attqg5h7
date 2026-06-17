# 0
class Solution:
    # Time: O(n)
    # Space: O(1)
    def climbStairs(self, n: int) -> int:
        j,k = 1,1
        current = 1
        for i in range(n-2, -1, -1):
            current = j + k
            k = j
            j = current
        
        return current
