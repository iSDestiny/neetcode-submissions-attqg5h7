class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start,end = intervals[i]

            print(prev_end)
            # non overlapping
            if start >= prev_end:
                prev_end = end
            else:
                count += 1
                prev_end = min(prev_end, end)
            print(prev_end)
            print("------")

        return count