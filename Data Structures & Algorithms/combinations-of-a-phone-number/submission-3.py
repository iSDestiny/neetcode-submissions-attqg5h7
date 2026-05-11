class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        res = []
        # Time: O(n * 4^n) where n is the length of digits
        # Space: O(n) extra space since the recursion depth is bounded by n (terminates for i >= len(digits))
        def dfs(i: int, curr: str):
            if i >= len(digits):
                res.append(curr)
                return
            # worst case 4^n decisions (for 9)
            for c in digitToChar[digits[i]]:
                dfs(i+1, curr+c)
        dfs(0, "")
        return res