from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    # Time: O(nlogk)
    # Space: O(n)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     heap = []
    #     freq = defaultdict(int)
    #     for n in nums:
    #         freq[n] += 1
    #     res = []
    #     for key in freq:
    #         heappush(heap, (freq[key], key))
    #         if len(heap) > k:
    #             heappop(heap)
    #     return [node[1] for node in heap]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        buckets = [[] for _ in range(max(freq.values())+1)]
        
        for key in freq:
            buckets[freq[key]].append(key)
        
        res = []
        for bucket in range(len(buckets)-1, 0, -1):
            if len(res) == k:
                return res
            for n in buckets[bucket]:
                res.append(n)
        return res