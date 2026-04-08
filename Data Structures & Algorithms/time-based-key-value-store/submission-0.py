from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append( (timestamp, value) )

    def get(self, key: str, timestamp: int) -> str:
        searchList = self.map[key]
        l, r = 0, len(searchList) - 1

        mostRecentTimestamp = (0, "")

        while l <= r:
            m = (l + r) // 2

            midTime, midValue = searchList[m]

            if timestamp == midTime:
                return midValue
            elif timestamp > midTime:
                mostRecentTimestamp = max(mostRecentTimestamp, (midTime, midValue)) 
                l = m + 1
            else:
                r = m - 1
        
        return mostRecentTimestamp[1]
