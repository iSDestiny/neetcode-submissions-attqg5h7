class Solution:
    # This can be represented as a graph where the vertices are the courses and the edges are the prerequisites
    # The problem is asking for a way to visit all the vertices in the graph in order (directional graph)
    #
    # To solve this problem we can use topological sort to take all the courses in a valid order, for the implementation
    # I plan to use Kahn's algorithm BFS where I will first build the adjacency list and an indegree dictionary to
    # track the number of incoming edges each course has. With the algorithm I will only process the courses with 0
    # incoming edges (this means that it has no prerequisites), once I visit these courses I will subtract the
    # number of indegrees from all of its children (i.e. if we visit 0 the indegrees for 1 will go down to 0) and
    # the next set of courses we will take is any new course with an indegree of 0. While performing this BFS I will maintain
    # a list of all courses processed and at the end this will be the solution if the length of the list is equal to the numCourses,
    # if it's not then this means there was a cycle (i.e. [[1,0], [0,1]]) which makes it impossible to take every course, here we will
    # return an empty array
    #
    # Time: O(V+E) where v is the number of courses (vertices) and e is the number of prerequisites (edges)
    # Space: O(V+E)

    from collections import deque

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list
        adjList = {} # gonna use a set for O(1) checks
        indegrees = {}

        # initialization
        for i in range(numCourses):
            adjList[i] = set()
            indegrees[i] = 0
        
        # create adj list + indegrees
        for u, v in prerequisites:
            adjList[v].add(u)
            indegrees[u] += 1
        
        queue = deque([u for u in indegrees if indegrees[u] == 0])

        order = []
        while queue:
            course = queue.popleft()
            order.append(course)

            for edge in adjList[course]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                    queue.append(edge)

        return order if len(order) == numCourses else []