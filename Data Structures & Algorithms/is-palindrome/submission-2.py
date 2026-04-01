import re

class Solution:
    # s: Was it a car or a cat I saw?
    # NOTE: case insensitive + ignore all non-alphanumeric
    # sNew: wasitacaroracatisaw
    # two pointers a and b where a starts at index 0 and iterates forward and b starts at the end and interates backwards
    #       a ->            <-b
    # sNew: wasitacaroracatisaw
    # Time: O(n)
    # Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        sNew = "".join(char for char in s.lower() if char.isalnum())
        a = 0
        b = len(sNew)-1

        while a < b:
            if sNew[a] != sNew[b]:
                return False
            a+=1
            b-=1
        return True
