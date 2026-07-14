class Solution:
    # Time: O(n)
    # Space: O(1)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mergable = []
        for a,b,c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            mergable.append([a,b,c])
        
        if not mergable:
            return False
        if mergable[0] == target:
            return True
        a,b,c = mergable[0]
        for i in range(1,len(mergable)):
            a2,b2,c2 = mergable[i]
            a,b,c = max(a,a2), max(b,b2), max(c,c2)

        return a == target[0] and b == target[1] and c == target[2]