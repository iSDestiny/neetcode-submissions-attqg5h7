from heapq import heappush, heappop, heapify
from collections import defaultdict

# Time: O(nlogn)
# Space: O(n)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_count = defaultdict(int)
        available_room = list(range(n))
        heap = []

        for start, end in sorted(meetings, key=lambda x: x[0]): # O(nlogn)
            while heap and heap[0][0] <= start:
                _, free_room = heappop(heap)
                heappush(available_room, free_room)
            if len(heap) == n:
                free_end, free_room = heappop(heap)
                heappush(available_room, free_room)
                delay = free_end - start
                end = end + delay

            next_room = heappop(available_room)
            heappush(heap, (end, next_room))
            room_count[next_room] += 1
        
        best_count = 0
        best_room = 0
        for room in range(n): # O(n)
            if room_count[room] > best_count:
                best_count = room_count[room]
                best_room = room
        return best_room