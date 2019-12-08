# n,m = map(int,input().split())
# # n为配料总数 m为钱数
#
# stors = [int(c) for c in input().split()]
# prices = [int(c) for c in input().split()]
#
# raws = []
# for i in range(len(stors)):
#     raws.append([stors[i],prices[i]])

#思路：将原料按原料数量及原料价格一起排序，先正序排原料数量，若数量相同再正序排原料价格
#      用一个堆栈来维护，结果输出堆栈里最小的原料数量

import heapq as hq
n,m = 3, 10
raws = [[5,15],[5,20],[5,20]]
# 堆栈排序结构
class tup:
    def __init__(self,num,val):
        self.num = num
        self.val = val
    # 改写__lt__方法实现结构体排序
    def __lt__(self,other):#operator <
        if self.num < other.num:
            return True
        elif self.num == other.num:
            return self.val < other.val
heap = []
for raw in raws:
    hq.heappush(heap,tup(raw[0],raw[1]))

# 弹出第一最小原料数量的原料，判断当前钱是否够买
cur = hq.heappop(heap)
while m >= cur.val:
    # 更新当前钱数及原料状态
    m -= cur.val
    tmp = cur.num + 1
    hq.heappush(heap,tup(tmp,cur.val))
    if m >= cur.val:
        cur = hq.heappop(heap)
    else:
        break
rr = hq.heappop(heap)
print(rr.num)