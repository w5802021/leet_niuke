'''
一般的思路：Counter记录每个元素出现的次数，维护一个大顶堆，每次将对应的最大的两个数相减一次，知道最后堆中不存在任何数，即为yes

递推出的高级解法：Counter记录每个元素出现的次数,只要那个元素出现次数最多的数不大于总数的一半，总能通过上述一般思路得出yes

'''

from collections import Counter
T = int(input())

for _ in range(T):
    n = int(input())
    nums = [int(c) for c in input().split()]
    dic = Counter(nums)
    maxx = float('-inf')
    for k in dic:
        maxx = max(dic[k],maxx)

    if maxx > n/2:
        print('NO')
    else:
        print('YES')




