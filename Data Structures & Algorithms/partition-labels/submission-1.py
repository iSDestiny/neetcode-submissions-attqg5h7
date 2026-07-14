# s = "xyxxyzbzbbisl"
# x: [0,3]
# y: [1,4]
# z: [5,7]
# b: [6,9]
# i: [10,10]
# s: [11,11]
# l: [12,12]

# Time: O(n) n = len(s)
# Space: O(m) m = unique letters in s
from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = defaultdict(int)
        for i in range(len(s)):
            end[s[i]] = i
        
        l = 0
        res = []
        while l < len(s):
            r = end[s[l]]
            size = 1
            while l < r:
                size += 1
                l += 1
                r = max(r, end[s[l]])
            l += 1
            res.append(size)
        return res
