class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        current = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if current[1] < interval[0]:
                res.append(current)
                current = interval
            else:
                current = [current[0], max(current[1], interval[1])]
        
        res.append(current)

        return res