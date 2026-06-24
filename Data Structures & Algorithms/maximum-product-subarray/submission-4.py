class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max(nums) 
        if len(nums) < 2:
            return global_max
        
        curr_min, curr_max = 1, 1
        for num in nums:
            if num == 0:
                curr_min = 1
                curr_max = 1
                continue
            withMax = num * curr_max
            withMin = num * curr_min
            curr_min = min(withMax, withMin, num)
            curr_max = max(withMax, withMin, num)
            global_max = max(global_max, curr_max)

        return global_max