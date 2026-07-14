# hand = [1,2,4,2,3,5,3,4], groupSize = 4
# minHeap = [(1,1), (2,2), (3,2), (4,2), (5,1)] = O(n)
# push/pop O(2logn) * number of groups (worst case n)
# [1,2,3,4], [2,3,4,5] -> True
#
# Constraints:
# - 1 <= len(hand) < +inf
# - 0 <= hand[i] < +inf
# - 1 <= groupSize <= len(hand)
#
# if len(hand) % groupSize != 0:
#    return False
# groups = len(hand) % groupSize
#
# Time: O(nlogn)
# Space: O(n)

from collections import defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = defaultdict(int)
        for num in hand:
            counts[num] += 1
        hand.sort() # O(nlogn)
        for num in hand:
            if counts[num] == 0:
                continue
            for i in range(num, num+groupSize):
                if counts[i] == 0:
                    return False
                counts[i] -= 1

        return True
