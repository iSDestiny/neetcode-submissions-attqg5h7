class Solution:
    # Time: O(n^3)
    # Space: O(n^2)
    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]
    #     cache = [[-1]*len(nums) for _ in range(len(nums))]

    #     def recurse(l: int, r: int) -> int:
    #         if l > r:
    #             return 0
    #         if cache[l][r] != -1:
    #             return cache[l][r]
    #         cache[l][r] = 0
    #         for i in range(l, r+1):
    #             current = nums[l-1] * nums[i] * nums[r+1]
    #             current += recurse(l, i-1) + recurse(i+1, r)
    #             cache[l][r] = max(cache[l][r], current)
    #         return cache[l][r]
        
    #     return recurse(1, len(nums)-2)
        
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n+2) for _ in range(n+2)]

        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    current = nums[l-1] * nums[i] * nums[r+1]
                    current += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], current)
        return dp[1][n]