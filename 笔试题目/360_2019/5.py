# n = int(input())
# A = [int(c) for c in input().split()]
# B = [int(c) for c in input().split()]
n = 5
A=[1,2,4,3,5]
B=[5,2,3,4,1]

def seq(nums):
    # stack是一个逐个存储nums的有序栈
    stack = [0] * len(nums)
    # 1、确定状态 当前迭代的最大长度
    maxl = 0
    # 4、计算顺序  自左向右
    for x in nums:
        # 3、初始边界条件
        # 当x不符合上升子序列时，maxl的值会减小，从而缩短了二分搜索的范围
        low, high = 0, maxl
        # 在stack中（二分搜索）找到一个位置插入x
        while low < high:
            mid = low + (high - low) // 2
            if stack[mid] < x:
                low = mid + 1
            else:
                high = mid
        # stack[:low]的长度  即为以x为子序列末尾的最大长度
        stack[low] = x
        # 2、状态转移方程
        maxl = max(low + 1, maxl)
    return maxl

C = [0 for _ in range(n+1)]
D = [0 for _ in range(n)]
#
for i in range(n):
    C[A[i]] = i+1
B= B[::-1]
for i in range(n):
    # 按B中的顺序，给A赋值
    # 1,3,4,2,5
    D[i] = C[B[i]]
# 此后相当于对D寻找最长上升子序列
print(seq(D))