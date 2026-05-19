class Solution:
    # Constraints:
    # len(intervals) >= 1
    # intervals is not sorted
    #
    # Time: O(nlogn)
    # Space: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        current_start, current_end = intervals[0] 
        for i in range(1, len(intervals)):
            start_i, end_i = intervals[i]

            if current_start > end_i or current_end < start_i:
                res.append([current_start, current_end]) # we're done with current, can't merge it anymore with others
                current_start, current_end = start_i, end_i
            else:
                current_start, current_end = min(current_start, start_i), max(current_end, end_i)

        res.append([current_start, current_end]) 
        return res
