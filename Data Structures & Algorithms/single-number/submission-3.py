class Solution:
    # Time: O(n)
    # Space: O(n)
    # from collections import defaultdict
    # def singleNumber(self, nums: List[int]) -> int:
    #     exists = defaultdict(int)
    #     for n in nums:
    #         exists[n] += 1
        
    #     for n in nums:
    #         if exists[n] == 1:
    #             return n
        
    # Time: O(n)
    # Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res