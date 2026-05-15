from collections import defaultdict, deque

class Solution:
    # A graph is a valid tree if it has these two properties:
    # - acyclic
    # - no disjoint sets (is a tree not a forest), it's fully connected
    #
    # Due to the properties above we can conclude that if a graph does not have n-1 edges exactly
    # it has a cycle, is disjoint, or both. If it does have n-1 edges exactly then 
    # it is either a valid tree or is a forest (not fully connected) with a cycle.
    # This means that if we know that there are n-1 edges then we can determine whether the graph
    # is a valid tree by checking if it has a cycle, if it doesn't then that means it's a valid tree
    #
    # We can solve this using one of the three ways:
    # - DFS to find the cycle
    # - BFS to find the cycle
    # - Union Find
    # All 3 are O(V+E) time and space V = n, E = len(edges)
    
    # DFS
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    #     if len(edges) != n-1:
    #         return False
        
    #     adjList = defaultdict(set)
    #     visiting = set()

    #     for u, v in edges:
    #         adjList[u].add(v)
    #         adjList[v].add(u)

    #     def noCycle(u: int, parent: int) -> bool:
    #         visiting.add(u)
    #         for v in adjList[u]:
    #             if v == parent:
    #                 continue
    #             if v not in visiting:
    #                 if not noCycle(v, u):
    #                     return False
    #             else:
    #                 return False
    #         return True
        
    #     return noCycle(0, -1) and len(visiting) == n
    # # BFS
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    #     if len(edges) != n-1:
    #         return False

    #     adjList = defaultdict(set)

    #     for u, v in edges:
    #         adjList[u].add(v)
    #         adjList[v].add(u)
        
    #     visited = set()
    #     queue = deque([[0, -1]])

    #     while queue:
    #         u, parent = queue.popleft()
    #         visited.add(u)
    #         for v in adjList[u]:
    #             if v == parent:
    #                 continue
    #             if v in visited:
    #                 return False
    #             queue.append([v, u]) 
        
    #     return len(visited) == n
    
    # Union Find
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        dsu = DSU(n)

        for u, v in edges:
            print(u,v)
            if not dsu.union(u, v):
                return False
        return True

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, a: int) -> int: # O(alpha(n)) -> O(1)
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    
    def union(self, a: int, b: int) -> bool: # O(alpha(n)) -> O(1)
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