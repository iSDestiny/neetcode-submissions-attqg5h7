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
    # Brute Force:
    # Time: O(n*n^n) -> O(n^2n) -> O(n^n)
    # Space: O(n)
    #
    # Top Down:
    # Time: O(n^2)
    # Space: O(n)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total // 2
        cache = [[None]*(half+1) for _ in range(len(nums)+1)] 
        def recurse(i: int, target: int) -> bool:
            if i == len(nums):
                return target == 0
            if target < 0:
                return False
            if cache[i][target] != None:
                return cache[i][target]
            cache[i][target] = recurse(i+1, target-nums[i]) or recurse(i+1, target)
            return cache[i][target]
        return any(recurse(i, half) for i in range(len(nums))) 