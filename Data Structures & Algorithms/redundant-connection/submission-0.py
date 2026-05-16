
# Union Find: O(alpha(n)) effectively O(1) * N times where N is the length of edges
# Time: O(n*alpha(n)) -> O(n)
# Space: O(n)

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n+1)) # since it's 1 based index 0 is not used at all
        self.rank = [0] * (n+1)
        self.count = n
    
    def find(self, a: int) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a]) # path compression optimization to guarantee O(alpha(n)) effectively constant time operations
        return self.parent[a]
    
    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        
        for u, v in edges:
            if not dsu.union(u, v):
                return [u,v]
        
        return []