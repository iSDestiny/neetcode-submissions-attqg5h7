# 0
class Solution:
    # Time: O(n)
    # Space: O(n)
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+2)

        for i in range(n, -1, -1):
            if i == n or i == n-1:
                dp[i] = 1
                continue
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]
