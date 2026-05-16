# 
# This is a shortest path from a source node in a directed graph with positive weights
#
# Time: O((V+E)log(v))
# Space: O(V+E)

from collections import defaultdict
from heapq import heappush,heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adjacency list
        adjList = defaultdict(list)
        for ui, vi, ti in times:
            adjList[ui].append((vi, ti))
        
        distances = [float('inf')]*(n+1)
        distances[k] = 0
        heap = [(0, k)]

        # djikstra
        while heap:
            du, u = heappop(heap)
            if du > distances[u]:
                continue
            for v, dv in adjList[u]:
                if du + dv < distances[v]:
                    distances[v] = du + dv
                    heappush(heap, (du+dv, v))
        sol = max(distances[1:])
        print(distances[1:])
        if sol == float('inf'):
            return -1
        return sol
