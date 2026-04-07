class Solution:
    # [6,1,2,3,4,5]
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        lowest = float('inf')
        while l <= r:
            m = (l + r) // 2
            lowest = min(lowest, nums[m])

            if nums[m] >= nums[r]:
                l = m+1
            else:
                r = m-1
        
        return int(lowest)
            