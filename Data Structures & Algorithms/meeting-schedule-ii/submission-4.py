"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        maxRooms = 0
        rooms = 0
        i, j = 0,0
        while i < len(start):
            if start[i] < end[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            maxRooms = max(maxRooms, rooms)
        return maxRooms
 