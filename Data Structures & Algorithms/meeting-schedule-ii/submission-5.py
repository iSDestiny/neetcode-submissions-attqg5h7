"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Time: O(nlogn)
# Space: O(n)
from heapq import heappush, heappop, heapify
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []

        for ival in sorted(intervals, key=lambda x: x.start):
            if heap and heap[0] <= ival.start:
                heappop(heap)
            heappush(heap, ival.end)
        return len(heap)

