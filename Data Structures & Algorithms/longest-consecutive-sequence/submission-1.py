class Solution:
    # consecutiveDict = {2: 3, 20: 21, 4: 5, 10: 11, 3: 4, 4:5, 5:6} O(n) to create this dict
    # consecutiveDict[2] -> consecutiveDict[3] -> consecutiveDict[4] -> consecutiveDict[5] -> O(n) if visited check is in place
    # O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        conDict = {}
        visited = set()
        for n in nums:
            conDict[n] = n+1
        
        longest = 0
        for n in nums: # O(n) = O(n+n)->O(2n)->O(n)
            previousN = n-1
            current = n
            if previousN not in visited: 
                conLength = 0
                while current in conDict: # O(n) cumulative so O(n+n) not O(n^2)
                    conLength += 1
                    visited.add(current)
                    current = conDict[current]
                longest = max(conLength, longest)
        return longest