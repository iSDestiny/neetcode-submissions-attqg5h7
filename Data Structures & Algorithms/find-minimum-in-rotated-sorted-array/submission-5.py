
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
        minVal = float("+inf")
        while start <= end:
            mid = (start + end) // 2
            minVal = min(minVal, nums[mid])
            if nums[start] <= nums[mid]:
                if nums[mid] <= nums[end]:
                    end = mid - 1
                else:
                    start = mid+1
            else:
                end = mid - 1
        print(start,end)
        return minVal