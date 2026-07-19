from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = []
        self.occurences = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.occurences[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0 
        seen = {(x,y) for x,y in self.points}
        x1,y1 = point
        for x2,y2 in self.points:
            if x1 == x2 or y1 == y2:
                continue
            if (x1,y2) not in seen or (x2,y1) not in seen:
                continue
            if abs(x1-x2) == abs(y1-y2):
                res += self.occurences[(x1,y2)] * self.occurences[(x2,y1)]
        return res