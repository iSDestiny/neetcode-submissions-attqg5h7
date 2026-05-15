class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.count = n
    
    # Time: O(alpha(n)) -> effectively O(1)
    def find(self, a: int) -> int:
        if self.parent[a] != a: # path compression
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    # Time: O(alpha(n)) -> effectively O(1)
    def union(self, a: int, b: int) -> bool:
        ra,rb = self.find(a), self.find(b)
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)    

        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.count