class Solution:
    # nums = [1,2,3,4]
    # totalSum = 10, half = 5
    #
    # find a subset that sums up to 5
    #
    # [1,2,3,4]
    #  ^     ^
    #
    # 1 -> 3 -> 6 False
    #        -> 7 False
    #   -> 4 -> 8 False
    #   -> 5 True
    #
    # Time: O(n*n^n) -> O(n^2n) -> O(n^n)
    # Space: O(n)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total / 2
        def recurse(i: int, target: int) -> bool:
            if i == len(nums):
                return False
            for j in range(i, len(nums)):
                if target - nums[j] == 0:
                    return True
                if target - nums[j] > 0 and recurse(j+1, target-nums[j]):
                    return True
        return any(recurse(i, half) for i in range(len(nums))) 