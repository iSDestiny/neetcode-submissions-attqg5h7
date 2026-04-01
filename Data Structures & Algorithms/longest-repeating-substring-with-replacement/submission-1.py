from collections import defaultdict

class Solution:
    # Time: O(n)
    # Space: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        # freq = defaultdict(int)
        # maxFreq = 0
        # start = 0
        # longest = 0
        # for end in range(len(s)):
        #     freq[s[end]] += 1
        #     maxFreq = max(maxFreq, freq[s[end]])
        #     windowSize = (end-start+1) - maxFreq
        #     while windowSize > k:
        #         freq[s[start]] -= 1
        #         start += 1
        #     longest = max(longest, end-start+1)
        # return longest
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res