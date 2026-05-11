class Solution:
    # "aab"
    # "" -> "a" (valid) -> add result and start new ["a"], "a" -> ["a", "a"], "b" -> ["a", "a", "b"]
    #                                                          -> ["a"], "ab" -> "ab" is INVALID
    #                   -> don't add result and keep for next iteration [], "aa" -> ["aa"], "b" -> ["aa", "b"]
    #                                                                            -> [], "aab" -> "aab" is INVALID
    
    # Time: O(n) where n is length of s
    def valid_palindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        def dfs(i: int, sub: str):
            if i >= len(s):
                if self.valid_palindrome(sub):     # commit trailing piece
                    current.append(sub)
                    res.append(current[:])
                    current.pop()
                return
            # Option 1: commit sub (only if it's a palindrome), then start a new one
            if sub and self.valid_palindrome(sub):
                current.append(sub)
                dfs(i + 1, s[i])
                current.pop()
            # Option 2: keep growing sub — no palindrome check, growth might fix it
            dfs(i + 1, sub + s[i])
        dfs(0, "")
        return res