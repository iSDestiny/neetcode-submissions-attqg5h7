from heapq import heappush_max, heappop_max, heapify_max
from collections import defaultdict, deque

class Solution:
    # Time: O(m) where m is the length of tasks
    # Space: O(m)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1
        
        heap = list(freq.values())
        heapify_max(heap)

        cooldown = deque()

        step = 0
        while heap or cooldown:
            step += 1 
            if heap:
                task_count = heappop_max(heap) - 1
                if task_count > 0:
                    cooldown.append((task_count, step+n))
            else:
                step = cooldown[0][1]
            while cooldown and cooldown[0][1] <= step:
                cd = cooldown.popleft()
                heappush_max(heap, cd[0])
        return step
                
            

        