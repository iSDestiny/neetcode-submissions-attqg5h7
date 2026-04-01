class Solution:
    # Time: O(n)
    # Space: O(n)
    #
    # stack = []
    # opening parens: '(', '{', '['
    #
    # ex: "([{}])"
    # stack = []

    # ex: ")("
    # stack = []
    # immediately return false since can't close )

    def isValid(self, s: str) -> bool:
        stack = []

        matchingParens = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != matchingParens[c]:
                    return False
        return len(stack) == 0