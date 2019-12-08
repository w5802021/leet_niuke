def maxEnvelopes(envelopes):
    '''
    动态规划
    :param envelopes:
    :return:
    '''
    # w宽度 h高度
    def custom_sort(x, y):
        if x[0] > y[0]:
            return 1
        if x[0] < y[0]:
            return -1
        if x[1] > y[1]:
            return 1
        if x[1] < y[1]:
            return -1
        return 0
    import functools
    # 自定义排序法
    envelopes = sorted(envelopes, key = functools.cmp_to_key(custom_sort))
    n = len(envelopes)
    dp = [1]*len(envelopes)
    res = 0
    for i in range(n):
        for j in range(i):
            if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i],dp[j]+1)
        res = max(dp[i],res)

    return res

def maxEnvelopes1(envelopes):
    '''
    动态+二分查找
    :param envelopes:
    :return:
    '''
    envelopes = sorted(envelopes, key = lambda x:(x[0],-x[1]))
    nums = []
    for i in envelopes:
        nums.append(i[1])
    stack = [0] * len(nums)
    maxl = 0
    for x in nums:
        low, high = 0, maxl
        while low < high:
            mid = low +(high - low) // 2
            if stack[mid] < x:
                low = mid + 1
            else:
                high = mid
        stack[low] = x
        maxl = max(low + 1, maxl)
    return maxl

if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,8],[6,7],[2,3]]
    print(maxEnvelopes(envelopes))