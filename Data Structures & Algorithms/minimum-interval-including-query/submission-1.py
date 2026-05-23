from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals and queries
        intervals.sort(key=lambda x: x[0])
        i = 0

        heap = []
        res = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heappush(heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][0], intervals[i][1]))
                i += 1
            while heap and heap[0][2] < q:
                heappop(heap)
            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]
