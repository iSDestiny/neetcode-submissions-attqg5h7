from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = defaultdict(int)

        for c in s:
            occurrences[c] += 1
        
        for c in t:
            occurrences[c] -= 1

        for key in occurrences:
            if occurrences[key] != 0:
                return False
        
        return True
