class Solution:
    #
    # s = "zxyzxy[y]"
    # set is used to store the window
    # maxSubLen = 3
    # Time: O(n)
    # Space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        windowSet = set()
        longestSub = 0

        for end in range(len(s)):
            while s[end] in windowSet:
                windowSet.remove(s[start])
                start += 1
            windowSet.add(s[end])
            longestSub = max(longestSub, end - start + 1)
        return longestSub