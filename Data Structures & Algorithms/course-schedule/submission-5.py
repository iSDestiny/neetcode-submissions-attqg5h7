from collections import deque

class Solution:
    # Time: O(n+m)
    # Space: O(n+m)
    # Top Sort (Kahn's):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj list
        adjList = {i: [] for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}
        for u,v in prerequisites:
            adjList[v].append(u)
            indegrees[u] += 1
        
        queue = deque([k for k in indegrees if indegrees[k] == 0])

        ops = 0
        while queue:
            u = queue.popleft()
            ops += 1
            for v in adjList[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
        return ops == numCourses