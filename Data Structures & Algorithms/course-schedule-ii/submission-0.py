from collections import deque, defaultdict

class Solution:
    #  numCourses = 3, prerequisites = [[1,0]]
    #  
    #  0->1 
    #  2
    #
    #
    # Time: O(V+E) where V is numCourses and E is the length of prerequisites
    # Space: O(V+E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        indegrees = defaultdict(int)
        res = []
        adjList = defaultdict(set)

        # build the adj list
        for u, v in prerequisites:
            indegrees[u] += 1
            adjList[v].add(u)

        # initialize queue with all courses with 0 indegrees
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        
        # bfs
        while queue:
            course = queue.popleft()
            res.append(course)
            for edge in adjList[course]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                    queue.append(edge)
        
        if len(res) != numCourses:
            return []
        return res