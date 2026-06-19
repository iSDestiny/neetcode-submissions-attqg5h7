class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(l,r) -> int: # O(n)
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        palindromes = 0
        for i in range(len(s)): # O(n^2)
            palindromes += isPalindrome(i, i+1) + isPalindrome(i,i)
        return palindromes
        