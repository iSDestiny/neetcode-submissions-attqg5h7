from collections import defaultdict

class Solution:
    #
    # numCourses = 2, prerequisites = [[0,1]]
    # 1 -> 0
    # True
    #
    # numCourses = 2, prerequisites = [[0,1],[1,0]]
    # 1 <-> 0
    # False due to the cycle
    #
    # numCourses = 3, prerequisites = [[0,1]]
    # 
    # 1 -> 0
    # 2
    # True
    
    # Time: O(n+m) n = numCourses, m = len(prerequisites)
    # Space: O(n+m)
    #
    # Perform a cycle detection on a graph using DFS if a cycle is found return False, else return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for p in prerequisites:
            adjList[p[0]].add(p[1])
        print(adjList)
        
        def dfs(v: int, visited: set) -> bool:
            if v in visited:
                return False
            visit = True
            visited.add(v)
            for e in adjList[v]:
                visit = visit and dfs(e, visited)
            visited.remove(v) 
            return visit

        for v in range(numCourses):
            if not dfs(v,set()):
                return False
        return True