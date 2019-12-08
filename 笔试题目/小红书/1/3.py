n = int(input())
baowu = []
for i in range(n):
    baowu.append(list(map(int,input().split())))

def maxEnvelopes1(baowu):
    '''
    动态+二分查找
    思路：同leetcode354 唯一不同的是这里要求只要不小于即可，不需要一定大于前一个选的物品
    :param envelopes:
    :return:
    '''
    baowu.sort(key=lambda x: (x[0], -x[1]))
    nums = []
    for i in baowu:
        nums.append(i[1])
    stack = [0] * len(nums)
    maxl = 0
    for x in nums:
        low, high = 0, maxl
        while low < high:
            mid = low +(high - low) // 2
            if stack[mid] <= x:
                low = mid + 1
            else:
                high = mid
        stack[low] = x
        maxl = max(low + 1, maxl)
    return maxl

print(maxEnvelopes1(baowu))




