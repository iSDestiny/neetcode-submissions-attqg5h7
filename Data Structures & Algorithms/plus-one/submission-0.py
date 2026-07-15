class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        if digits[-1] == 10:
            digits[-1] = 0
            carry = 1
        i = len(digits)-2
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
