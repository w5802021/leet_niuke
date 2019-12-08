import heapq as hq
# 堆接口

'''
#向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质
heapq.heappush(heap, item)

#heapq把列表x转换成堆
heapq.heapify(x)

#从可迭代的迭代器中返回最大的n个数，可以指定比较的key
heapq.nlargest(n, iterable[, key])

#从可迭代的迭代器中返回最小的n个数，可以指定比较的key
heapq.nsmallest(n, iterable[, key])

#从堆中删除元素，返回值是堆中最小或者最大的元素
heapq.heappop(heap)
'''


######################## heappush创建堆
nums = [0,2,1,4,3,9,5,8,6,7]
heap = []
for num in nums:
    hq.heappush(heap, num)  # 加入堆
hq.heappop(heap)
a = 1
# print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
# print([hq.heappop(heap) for _ in range(len(nums)-1)])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]


# ######################### heapify创建堆   heappop
# nums = [2, 3, 5, 1, 54, 23, 132]
# hq.heapify(nums)
# hq.heappop(nums)
# # print()
# print([hq.heappop(nums) for _ in range(len(nums)-1)])  # 堆排序结果
# # out: [1, 2, 3, 5, 23, 54, 132]
#
#
# #########################  merge合并堆
#
# num1 = [32, 3, 5, 34, 54, 23, 132]
# num2 = [23, 2, 12, 656, 324, 23, 54]
# num1 = sorted(num1)
# num2 = sorted(num2)
# # 合并两个已经排序好的[iterables]
# res = hq.merge(num1, num2)
# print(list(res))
#
# ########################  nlargest  nsmallest
#
# nums = [1, 3, 4, 5, 2]
# print(hq.nlargest(3, nums))
# print(hq.nsmallest(3, nums))
#
#
# '''
# 堆排序自定义比较
# '''
# #heapq使用的内置的小于号，或者类的__lt__比较运算来进行比较
# def heapq_int():
#     # 初始化数值
#     heap = []
#     #以堆的形式插入堆
#     hq.heappush(heap,10)
#     hq.heappush(heap,1)
#     hq.heappush(heap,10/2)
#     [hq.heappush(heap,i) for i in  range(10)]
#     [hq.heappush(heap,10 - i) for i in  range(10)]
#     print (hq.nlargest(10,heap))
#     print ([hq.heappop(heap) for i in range(len(heap))])
#
# def heapq_tuple():
#     # 初始化元组
#     heap = []
#     hq.heappush(heap,(10,'ten'))
#     hq.heappush(heap,(1,'one'))
#     hq.heappush(heap,(10/2,'five'))
#     while heap:
#         print (hq.heappop(heap))
#
# class tup:
#     def __init__(self,priority,description):
#         self.priority = priority
#         self.description = description
#     # 改写__lt__方法实现结构体排序
#     def __lt__(self,other):#operator <
#         return self.priority < other.priority
#
#     # def __ge__(self,other):#oprator >=
#     #     return self.priority >= other.priority
#     # def __le__(self,other):#oprator <=
#     #     return self.priority < other.priority
#     # 自定义比较函数
#     # def __cmp__(self,other):
#     #     #call global(builtin) function cmp for int
#     #     return cmp(self.priority,other.priority)
#     # def __str__(self):
#     #     return '(' + str(self.priority)+',\'' + self.description + '\')'
#
# def heapq_class():
#     heap  = []
#     hq.heappush(heap,tup(100,'proficient'))
#     hq.heappush(heap,tup(10,'expert'))
#     hq.heappush(heap,tup(11,'novice'))
#     while heap:
#         print (hq.heappop(heap))
# if __name__ == '__main__':
#     heapq_class()







