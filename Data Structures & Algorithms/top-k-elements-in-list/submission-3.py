from collections import defaultdict

class Solution:
    # Example 1: nums = [1,2,2,3,3,3], k = 2
    # [ [], [1], [2], [3], [], [], [] ] -> O(2n)
    # [ [1,2,3,4,5,6], [], [ ], [], [], [], [] ] -> O(n)
    # picking the top K elements from ^ O(n)
    # O(2n) -> O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1

        for num in freqs:
            freq = freqs[num]
            buckets[freq].append(num)
        
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        

