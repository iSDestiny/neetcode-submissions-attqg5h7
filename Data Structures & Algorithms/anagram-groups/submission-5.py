# constraints: 
# len(strs) >= 0 edge case empty list (return empty list)
# strs[i] made up of lowercase English letters
# 0 <= sts[i] <= 1000 if empty word then this just means we will have a separate grouping for it (i.e. ["", "abc"] -> [[""], ["abc"]])
#
# Time: O(n*c) where n is length of strs and c is length of the longest word
from collections import defaultdict
class Solution:
    # strs = ["hat", "act", "cat"]
    # output = [["hat"],["act", "cat"]]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list) # {(..., 1, .., 1 ..., 1): ["hat"], (1,...1,....1): ["act", "cat"]} # hat

        for word in strs: # hat
            freq = [0] * 27 # {h: 1, a: 1, t: 1}
            for c in word: # runs c times; h, a, t
                freq[ord(c)-ord('a')] += 1 # to get the 0 based index
            groupings[tuple(freq)].append(word) # runs c times to convert freq to tuple

        return list(groupings.values())