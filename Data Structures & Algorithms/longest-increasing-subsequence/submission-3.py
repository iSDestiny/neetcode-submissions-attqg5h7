class Solution:
    # Recursion:
    # - For each index i in nums
    #.  - iterate nums from i to len(nums): j
    #.     - if nums[j] > nums[i]:
    #          - choose to include it in the subsequence and then perform a recursion recurse(j)
    #          - skip it and continue checking to include the other values instead
    #      - else if iteration finishes and none is found recurse on recurse(i+1):
    #          - skip and continue checking
    #      return the maximum sequence length
    # Brute Force:
    # Time: O(n*n^n) -> O(n^2n) -> O(n^n)
    # Space: O(n)
    # Top Down:
    # Time: O(n^2)
    # Space: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def recurse(i: int) -> int:
            if i == len(nums):
                return 0
            if cache[i] > -1:
                return cache[i]
            max_seq = 1 # min is including self
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_seq = max(max_seq, 1 + recurse(j))
            cache[i] = max_seq
            return cache[i]
        return max(recurse(i) for i in range(len(nums)))