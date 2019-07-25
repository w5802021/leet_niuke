# Definition for an interval.
class node:
    def __init__(self, s, e):
        self.start = s
        self.end = e

def eraseOverlapIntervals(intervals):
    intervals = sorted(intervals, key = lambda x:(x[0]))
    res = 0
    end = -float('inf')
    for x in intervals:
        if x[0] < end:
            end = min(end, x[1])
            res += 1
        else:
            end = x[1]
    return res

def eraseOverlapIntervals1(intervals):

    end = float('-inf')
    erased = 0
    for i in sorted(list(intervals), key=lambda i: i.end):
        if i.start >= end:
            end = i.end
        else:
            erased += 1
    return erased

if __name__ == '__main__':
    l =[[1,2]]

    print(eraseOverlapIntervals1(l))