
# [3,4,5,6,1,2]
#      ^ ->
# [5,1,2,3,4]  
#      ^
# Time: O(logn)
# Space: O(1)  
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("nums can't be empty")

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid+1
        return nums[start]