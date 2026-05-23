# [3,2,1]
# [1] [2,3]
# 
# [3,2,1,5]
# [1,2] [3,5] = (max(A) + min(B))/2
#   ^max ^min
#
#

from heapq import heappush, heappop, heappush_max, heappop_max

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush_max(self.small, num)
        # rebalance
        while abs(len(self.large) - len(self.small)) > 1:
            if len(self.large) > len(self.small):
                p_num = heappop(self.large)
                heappush_max(self.small, p_num)
            else:
                p_num = heappop_max(self.small)
                heappush(self.large, p_num)
        

    def findMedian(self) -> float:
        # print(self.small, self.large)
        if (len(self.small) + len(self.large)) % 2 == 0:
            return (self.small[0] + self.large[0]) / 2
        else:
            return self.small[0] if len(self.small) > len(self.large) else self.large[0]
        