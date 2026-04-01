class Solution:
    # Time: O(n)
    # Space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()

                result = 0
                if t == "+":
                    result = left + right
                elif t == "-":
                    result = left - right
                elif t == "*":
                    result = left * right
                else:
                    result = int(left / right)
                
                stack.append(result)
        
        return stack[-1]