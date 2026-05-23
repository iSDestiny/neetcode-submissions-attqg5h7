"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import  heappop, heapify

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startHeap = []
        endHeap = []

        for interval in intervals:
            startHeap.append(interval.start)
            endHeap.append(interval.end)

        heapify(startHeap)
        heapify(endHeap)

        count = 0
        maxCount = 0
        while startHeap:
            if endHeap[0] <= startHeap[0]:
                count -= 1
                heappop(endHeap)
            else:
                count += 1
                heappop(startHeap)
            maxCount = max(maxCount, count)      
        
        return maxCount

