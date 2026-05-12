class Solution:
    # [1,2,4,6]
    # left = [1,1,2,8]
    # right = [48,24,6,1]
    # output = [left[i]*right[i], left[i+1]*right[i+1]]
    # output = [48,24,12,8]
    # Time: O(n)
    # Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        left = [1]*(len(nums)+1)
        right = [1]*(len(nums)+1)

        # build left
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        # build right
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        print(left, right)
        output = [1] * len(nums)
        # build output
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        return output