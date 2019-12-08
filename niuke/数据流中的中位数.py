from heapq import *

class Solution:
    def __init__(self):
        self.low = []
        self.high = []

    def Insert(self, num):
        # write code here
        heappush(self.high, -heappushpop(self.low, -num))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def GetMedian(self, n=None):
        # write code here
        return float(-self.low[0]) if len(self.low) > len(self.high) else (-self.low[0] + self.high[0]) / 2.0