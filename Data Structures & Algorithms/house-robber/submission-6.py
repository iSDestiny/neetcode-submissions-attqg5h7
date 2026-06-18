class Solution:
    # brute force: 
    #   time: O(2^n)
    #   space: O(n)
    # memoization:
    #   time: O(n)
    #   space: O(n)
    # def rob(self, nums: List[int]) -> int:
    #     cache = [-1] * len(nums)
    #     def recurse(i: int) -> int:
    #         if i >= len(nums):
    #             return 0
    #         if cache[i] != -1:
    #             return cache[i]
    #         rob_current = nums[i] + recurse(i+2)
    #         skip_current = recurse(i+1)
    #         cache[i] = max(rob_current, skip_current)
    #         return cache[i]
        
    #     return recurse(0)

    # [1,1,3,3]
    # dp: [4,4,3,3,0,0]
    # DP:
    #   time: O(n)
    #   space: O(1)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob_current = 0
        skip_current = 0
        for i in range(n-1, -1, -1):
            temp = max(skip_current, nums[i] + rob_current)
            rob_current = skip_current
            skip_current = temp
        return max(skip_current, rob_current)