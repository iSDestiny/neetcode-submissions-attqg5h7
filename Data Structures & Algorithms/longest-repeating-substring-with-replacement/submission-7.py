from collections import defaultdict

class Solution:
    # Time: O(n)
    # Space: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxFreq = 0
        start = 0
        longest = 0
        for end in range(len(s)):
            freq[s[end]] += 1
            maxFreq = max(maxFreq, freq[s[end]])
            windowSize = (end-start+1) - maxFreq
            while windowSize > k:
                freq[s[start]] -= 1
                start += 1
                windowSize = (end-start+1) - maxFreq
            longest = max(longest, end-start+1)
        return longest
