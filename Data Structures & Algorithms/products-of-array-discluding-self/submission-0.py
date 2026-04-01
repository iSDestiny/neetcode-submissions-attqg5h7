class Solution:
    # [1,2,4,6]
    # Prefix Prod: [1, 1, 2, 8], [48, 24, 6, 1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = []

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res