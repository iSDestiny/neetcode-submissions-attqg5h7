from collections import defaultdict

class Solution:
    # freqTuple = (0) * 27 -> cat: (1, 0, 1, ..... 1)
    # anagramGroups = { (freqTuple): ["cat", "act"] }
    # O(m) where m is the sum of the length of all strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)

        # O(m)
        for s in strs:
            freqList = [0] * 27
            # O(c)
            for c in s:
                charIndex = ord(c) - ord('a')
                freqList[charIndex] += 1
            # O(c) 
            freqTuple = tuple(freqList)
            anagramGroups[freqTuple].append(s)
        
        return [l for l in anagramGroups.values()]