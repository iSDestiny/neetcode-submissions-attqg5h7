# Inputs:
# n is the number of nodes (0 based, 0 -> n-1), src is the source node and dst is the destination node
# k is the maximum stops the shortest path can be
# flights is a list of edges + the edge weight. No negative edges, no self cycles, no duplicate edges
# constraints: 0 <= src, dst, k < n
#
# goal, find the shortest path from src to dst with at most k stops in the flight graph, return the shortest path's cost
#
#
# Examples:
#
# n = 4, flights = [[0,3,1000], [0,1,100], [1,2,100], [2,3,100]], k = 0, src = 0, dst = 3
#
# output = 1000
#
# explanation since k=0 only paths from 0 to 3 with 0 stops (direct flights) are considered
# and there only exists one direct path from 0 to 3 which is edge [0,3,1000], hence the cost is 1000 even though
# a longer but cheaper path 0 -> 1 -> 2 -> 3 (costs 300) exists
#
# if k = 2 then the output would change to 300
#
# Edge Case:
# If there is no path that exists from src to dst with at most K times then return -1
#
# n = 4, flights = [[0,1,100], [1,2,100], [2,3,100]], k = 0, src = 0, dst = 3
#
# output = -1
#
# Explanation: Since the only valid path from 0 to 3 has two stops 0 -> 1 -> 2 -> 3 then it's impossible to satisy k = 0
#
#
# This is a single source shortest path graph problem. There are two algorithms I'm considering to solve this solution: Djikstras and Bellman Ford.
# However, if since the shortest path is limited by K, I don't think Djikstras will work due to its greedy nature. When processing the edges
# of the example above djikstras will always greedily pick the local cheapest, if we ran a simulation it would pick the edge [0,1,100] and will not even
# walk the edge [0,3,1000] due to the greedy nature.
#
# Due to this, I think bellman ford is the approach I will choose even though it's of higher time complexity O(VE) vs O(ElogV)
#
#
# In bellman ford we will relax every edge V - 1 times. In order to satisfy the at most K stops we will have to make a slight variation
# to the typical implementation where in one round of relaxation, when relaxing an edge say [0,1] we can use the value for that to relax [1,2].
# The variation will involve creating a local copy of the distances structure where we store the shortest paths for every node such that
# in one round edge relaxation cannot use the relaxed values of edges within the same round, this will guarantee that we are only adding
# one edge at a time when computing the shortest path from source to destination.
#
# With this information we can stop the amount of times we relax the edges at K+1 times and return the path cost to the dst after.
# The time complexity will be O(k*(E+V)) and space will be O(V)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[src] = 0

        for _ in range(k+1):
            newDist = distances.copy() # v times
            for u, v, c in flights: # E times
                vc = distances[u] + c
                if distances[u] != float('inf') and vc < newDist[v]:
                    newDist[v] = vc
            distances = newDist
        
        return distances[dst] if distances[dst] != float('inf') else -1