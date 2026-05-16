# Time: O(n^2logn)
# Space: O(n^2)

from typing import Tuple

class DSU:
    def __init__(self, points: List[List[int]]):
        self.parent = {(x,y): (x,y) for x,y in points}
        self.rank = {(x,y): 0 for x,y in points}
    
    def find(self, a: Tuple[int, int]) -> Tuple[int, int]:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a]) # path compression
        return self.parent[a]
    
    def union(self, a: Tuple[int,int], b: Tuple[int, int]) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                edges.append(((xi,yi), (xj,yj), abs(xi-xj) + abs(yi-yj)))
        edges = sorted(edges, key=lambda x: x[2])
        dsu = DSU(points)
        cost = 0
        for u, v, d in edges:
            if dsu.union(u, v):
                cost += d
        return cost