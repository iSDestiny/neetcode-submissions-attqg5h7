from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        want = defaultdict(int)
        for c in s1:
            want[c] += 1
        
        window = defaultdict(int)
        have = 0
        for end in range(len(s2)):
            end_char = s2[end]
            window[end_char] += 1

            if end_char in want:
                if want[end_char] == window[end_char]:
                    have += 1
                if want[end_char]+1 == window[end_char]:
                    have -= 1

            if have == len(want):
                return True

            start = end - len(s1) + 1
            if start < 0:
                continue

            start_char = s2[start] 
            window[start_char] -= 1
            
            if start_char in want:
                if window[start_char] == want[start_char] - 1:
                    have -= 1
                if window[start_char] == want[start_char]:
                    have += 1

        print(have)
        print(window)
        print(want)

        return False