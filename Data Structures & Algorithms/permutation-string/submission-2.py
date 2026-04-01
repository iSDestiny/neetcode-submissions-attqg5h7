class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1

        start = 0
        for end in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[end]) - ord('a')

            freq2[index] += 1
            if freq1[index] == freq2[index]:
                matches += 1
            elif freq1[index] + 1 == freq2[index]:
                matches -= 1
            
            indexl = ord(s2[start]) - ord('a')
            freq2[indexl] -= 1

            if freq1[indexl] == freq2[indexl]:
                matches += 1
            elif freq1[indexl] - 1 == freq2[indexl]:
                matches -= 1

            start += 1
        return matches == 26