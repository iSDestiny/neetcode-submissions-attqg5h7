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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adjList = defaultdict(set)
        visiting = set()

        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        def noCycle(u: int, parent: int) -> bool:
            visiting.add(u)
            for v in adjList[u]:
                if v == parent:
                    continue
                if v not in visiting:
                    if not noCycle(v, u):
                        return False
                else:
                    return False
            #visiting.remove(u)
            return True
        
        return noCycle(0, -1) and len(visiting) == n
    # BFS
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    #     if len(edges) != n-1:
    #         return False

    #     adjList = defaultdict(set)

    #     for u, v in edges:
    #         adjList[u].add(v)
    #         adjList[v].add(u)
        
