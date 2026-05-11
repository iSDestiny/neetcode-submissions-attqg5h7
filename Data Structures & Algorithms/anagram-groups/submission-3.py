from collections import defaultdict
# Time: O(n*m)
# Space: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        # O(n*m)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            # O(26)
            groups[str(freq)].append(s)
        return list(groups.values())