class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def recurse(i, n, cache) -> int:
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(recurse(i+1, n, cache), nums[i]+recurse(i+2, n, cache))
            return cache[i]

        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)
        return max(recurse(0, len(nums)-1, cache1), recurse(1, len(nums), cache2))