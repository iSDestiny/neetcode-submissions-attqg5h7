class Solution:
    # constraints
    #  - intervals does not contain any over lapping intervals
    #  - intervals is sorted in ascending order by the start time
    #  ^ facts above guarantees that end_i < start_i+1
    #  - len(intervals) >= 0 (if empty just return empty list)
    #  - len(newInterval) == 2
    #
    # intervals = [[1,3],[4,6]], newInterval = [2,5]
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            start_i, end_i = intervals[i]
            # does new interval go to the left?
            if new_end < start_i: 
                return res + [[new_start, new_end]] + intervals[i:]
            # does it go to the right?
            elif new_start > end_i:
                res.append(intervals[i]) # only append the current not the new yet
            # overlapping
            else:
                new_start, new_end = min(start_i, new_start), max(end_i, new_end)
        res.append([new_start, new_end])
        return res