class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        global_max = float("-inf")

        for i in range(len(nums)):
            # start new
            if current_max + nums[i] < nums[i]:
                current_max = nums[i]
            else:
                current_max += nums[i]
            global_max = max(global_max, current_max)
        
        return max(global_max, max(nums))