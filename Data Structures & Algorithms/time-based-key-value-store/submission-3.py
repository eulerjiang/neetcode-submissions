from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = [(timestamp, value)]
        else:
            self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""

        items = self.cache[key]

        l, r = 0, len(items) - 1

        result = ""

        while l <= r:
            mid = (l + r) // 2
            if items[mid][0] == timestamp:
                return items[mid][1]
            elif items[mid][0] < timestamp:
                result = items[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result

        
