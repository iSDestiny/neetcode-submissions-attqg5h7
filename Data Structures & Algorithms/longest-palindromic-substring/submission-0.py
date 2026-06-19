class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l,r) -> str:
            while l >= 0 and r < len(s):
                # print(s[l], s[r])
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l+1:r]
        
        resLength = 0
        currentRes = ""
        for i in range(len(s)):
            even = isPalindrome(i, i+1)
            odd = isPalindrome(i,i)
            if len(even) > resLength:
                resLength = len(even)
                currentRes = even
            if len(odd) > resLength:
                resLength = len(odd)
                currentRes = odd
            # print("===f=====")
        return currentRes
        
