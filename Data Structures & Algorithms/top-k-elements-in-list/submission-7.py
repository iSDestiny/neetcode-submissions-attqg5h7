from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    # Time: O(nlogk)
    # Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        res = []
        for key in freq:
            heappush(heap, (freq[key], key))
            if len(heap) > k:
                heappop(heap)
        return [node[1] for node in heap]