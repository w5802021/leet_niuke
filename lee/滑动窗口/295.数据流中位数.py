from heapq import *
class MedianFinder:
    

    def addNum(self, x):
        heappush(self.high, -heappushpop(self.low, -x))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self):
        return float(-self.low[0]) if len(self.low) > len(self.high) else (-self.low[0] + self.high[0]) / 2.0

