class Solution:
    # n = 3
    # "" -> "(" -> "((" -> "(((" -> "((()"
    #                   -> "(()" -> "(()())"
    #           -> "()"
    # keep track of the open and close parens with integers open and close
    # at every step make this decision and recurse:
    #   - add a "(" if open < n
    #   - add a ")" if there are enough open parens (close < open)
    # keep making these recursive decisions until its no longer possible (this is a final valid parens),
    # and append the final parens to the result
    # Time: O(n * 2^n)
    # Space: O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(paren: str, opening: int, close: int): 
            if opening == n and close == n:
                result.append(paren)
                return
            if opening < n:
                dfs(paren+"(", opening+1, close)
            if close < opening:
                dfs(paren+")", opening, close+1)
        dfs("", 0, 0)
        return result