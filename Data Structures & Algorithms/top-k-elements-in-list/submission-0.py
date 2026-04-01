from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        buckets = [[] for i in range(len(nums))]

        for n in set(nums):
            buckets[freq[n]-1].append(n)
        
        i = 0
        res = []
        for bucket in reversed(buckets):
            if i == k:
                return res
            for num in bucket:
                if i == k:
                    return res
                res.append(num)
                i +=1
        return res