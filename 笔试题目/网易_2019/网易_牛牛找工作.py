
class job:
    def __init__(self,diff,peny):
        self.d = diff
        self.p = peny
N, M = 3,3
dict = {1:100,10:1000,1000000000:1001}
jobs = [1,10,1000000000]

import bisect
jobs.sort()
guys = [9, 10, 1000000000]
res = []
for ai in guys:
    # 二分查找
    ind = bisect.bisect_right(jobs, ai)
    res.append(dict[jobs[ind-1]])
print(' '.join(str(c) for c in res))

