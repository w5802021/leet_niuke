import collections

def longestArithSeqLength(nums):
    dp = collections.defaultdict(int)

    for i in range(1, len(nums)):
        for j in range(i):    #j为等差数列前一个数下标
            if (nums[i] - nums[j], j) not in dp:  #这里代表i 代表后面数组中出现符合等差数列规律的数
                dp[(nums[i] - nums[j], i)] = 2
            else:
                dp[(nums[i] - nums[j], i)] = dp[(nums[i] - nums[j], j)] + 1

    return max(dp.values())

def longestArithSeqLength2(nums):      ###等待理解    速度很快
    idxs = collections.defaultdict(list)

    for i, v in enumerate(nums):
        idxs[v].append(i)

    ans = 0
    cnts = collections.Counter()

    for k in range(len(nums)):  # last
        for j in range(k):  # middle
            v = 2 * nums[j] - nums[k]  # first

            if v in idxs:
                for i in idxs[v]:
                    if i >= j: break
                    cnts[j, k] = max(cnts[j, k], cnts[i, j] + 1)
                    ans = max(ans, cnts[j, k])

    return ans + 2

if __name__ ==  '__main__':
    nums = [3,6,9,12]
    print(longestArithSeqLength(nums))
