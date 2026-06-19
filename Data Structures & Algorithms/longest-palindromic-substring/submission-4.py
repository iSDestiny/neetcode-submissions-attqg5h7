class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def longestPalindrome(self, s: str):
        def isPalindrome(l,r) -> str: # O(n)
            while l >= 0 and r < len(s):
                # print(s[l], s[r])
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return [l+1, r]
        
        resLength = 0
        currentRes = ""
        for i in range(len(s)): # O(n^2)
            l1,r1 = isPalindrome(i, i+1)
            l2,r2 = isPalindrome(i,i)
            if r1-l1+1 > resLength:
                resLength = r1-l1+1
                currentRes = s[l1:r1]
            if r2-l2+1 > resLength:
                resLength = r2-l2+1
                currentRes = s[l2:r2]
        return currentRes
        
