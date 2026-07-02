class Solution:
    # fn(i: int, total: int)
    # nums = [2,2,2], target = 2
    # fn(0, 0) -> fn(1, 2) -> fn(2, 4) -> fn(3, 6) -> 0
    #                                  -> fn(3, 2) -> 1
    #                      -> fn(2, 0) -> fn(3, 2)
    #                                   -> fn(3, -2) -> 0
    #          -> fn(1, -2) -> fn(2, 0) -> 1
    #                                   
    #                       -> fn(2, -2) -> fn(3, 0) -> 0
    #                                    -> fn(3, -4) -> 0
    # fn(0,0) = 3
    #
    # Time: O(2^n) -> O(n*m)
    # Space: O(n)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def recurse(i: int, total: int) -> int:
            if i >= len(nums):
                return 1 if total == target else 0
            key = (i, total)
            if key in cache:
                return cache[key]
            cache[key] = recurse(i+1, total + nums[i]) + recurse(i+1, total - nums[i])
            return cache[key]
        
        return recurse(0,0)