class Solution:
    # Time: O(n)
    # Space: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry > 0:
            if i == -1:
                digits.insert(0, carry)
                carry = 0
            else:
                digits[i] += carry
                carry = 0
                if digits[i] == 10:
                    carry = 1
                    digits[i] = 0
            i -= 1
        return digits
