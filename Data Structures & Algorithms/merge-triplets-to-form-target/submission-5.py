class Solution:
    # Time: O(n)
    # Space: O(1)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ra,rb,rc = -1,-1,-1
        for a,b,c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            ra,rb,rc = max(ra,a), max(rb,b), max(rc,c)
        
        return ra == target[0] and rb == target[1] and rc == target[2]