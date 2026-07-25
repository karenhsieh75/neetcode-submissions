class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)  # key: [[timestamp1, value1], [timestamp2, value2]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]

        if not values or timestamp < values[0][0]:
            return ""
        if timestamp >= values[-1][0]:
            return values[-1][1]

        l, r = 0, len(values)
        while l <= r:
            m = (l + r) // 2

            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] > timestamp:
                r = m - 1
            elif values[m][0] < timestamp and values[m + 1][0] > timestamp:
                return values[m][1]
            else:
                l = m + 1
        
        return ""
