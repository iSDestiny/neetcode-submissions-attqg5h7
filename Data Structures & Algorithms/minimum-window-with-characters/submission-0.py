# Input: s = "OUZOD[YXAZ]V", t = "XYZ"

# Output: "YXAZ"
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        freq_t = defaultdict(int)        
        for c in t:
            freq_t[c] += 1
        
        have, need = 0, len(freq_t)
        res, resLen = [-1,-1], float('inf')
        window = defaultdict(int)
        start = 0
        for end in range(len(s)):
            window[s[end]] += 1
            
            if s[end] in freq_t and window[s[end]] == freq_t[s[end]]:
                have += 1
            
            while have == need:
                if (end - start + 1) < resLen:
                    res = [start, end]
                    resLen = end - start + 1

                window[s[start]] -= 1
                if s[start] in freq_t and window[s[start]] < freq_t[s[start]]:
                    have -= 1
                start += 1
        
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""