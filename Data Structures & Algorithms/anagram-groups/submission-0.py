from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphaGroups = defaultdict(list)
        
        for word in strs:
            alpha = [0,]*27
            for letter in word:
                alpha[ord(letter)-ord('a')]+=1
            alphaGroups[tuple(alpha)].append(word)
        

        return [alphaGroups[key] for key in alphaGroups]
