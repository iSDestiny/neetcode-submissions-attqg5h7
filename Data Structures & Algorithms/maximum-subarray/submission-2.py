class Solution:
    # Time: O(n)
    # Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        global_max = float("-inf")
        start,end = 0,0

        for i in range(len(nums)):
            # start new
            if current_max + nums[i] < nums[i]:
                current_max = nums[i]
                start = i
            else:
                current_max += nums[i]
            if global_max < current_max:
                global_max = current_max
                end = i
        
        print(start,end)
        return global_max