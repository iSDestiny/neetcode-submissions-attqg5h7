# This is an undirected graph connectivity problem. The question is asking us to find the number of connected subsets within the graph
# To get this I will use Disjoint Set Union (aka Union Find) with path compression and union by rank to return the number of
# connected components in O(n+e*alpha(n)) effectively O(n+e) time and O(n) space


class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n
    
    def find(self, a: int) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra,rb = rb,ra
        
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)        

        for u,v in edges:
            dsu.union(u,v)
        
        return dsu.count