class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        moods = self.times[key]
        beg = 0
        end = len(moods) - 1
        ans = ""

        while beg <= end:
            mid = (beg + end ) // 2
            if moods[mid][0] <= timestamp:
                ans = moods[mid][1]
                beg = mid + 1
            else:
                end = mid -1
        return ans 
        
