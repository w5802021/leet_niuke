from collections import defaultdict,Counter

def longestArithSeqLength(nums):
    '''
    求最长的等差子序列的长度
    :param nums:
    :return:
    '''
    # 1、确定状态 三维dp[(j,i)]表示到达当前位置i,公差为j的等差数列的长度
    # 3、初始条件为空
    dp = defaultdict(int)
    # 4、计算顺序 自左向右
    for i in range(1, len(nums)):
        # j为nums[i]之前的数
        for j in range(i):
            # 这里代表i 代表后面数组中出现符合等差数列规律的数
            # 2、转移方程
            if (nums[i] - nums[j], j) not in dp:
                dp[(nums[i] - nums[j], i)] = 2
            else:
                dp[(nums[i] - nums[j], i)] = dp[(nums[i] - nums[j], j)] + 1
    return max(dp.values())

def longestArithSeqLength2(nums):
    # nums每个数的下标字典
    idx = defaultdict(list)
    for i, v in enumerate(nums):
        idx[v].append(i)
    ans = 0
    # 1、确定状态
    cnts = Counter()
    # 4、计算顺序  自左向右
    for k in range(1,len(nums)):
        for j in range(k):
            # nums[j]为等差数列中间数 nums[k]为等差数列靠后的数
            # v为等差数列靠前的数
            v = 2 * nums[j] - nums[k]
            if v in idx:
                # 可能出现nums中有重复数，其下标不同
                for i in idx[v]:
                    if i >= j:
                        break
                    # 2、状态转移矩阵
                    # cnts[j, k]表示到达当前nums[k]，以公差为（nums[k]-nums[j]），找到的v（属于数列中的数）的最大数量
                    # 因此最后结果还要加上nums[j]、nums[k]的长度
                    cnts[j, k] = max(cnts[j, k], cnts[i, j] + 1)
                    ans = max(ans, cnts[j, k])
    return ans + 2

if __name__ ==  '__main__':
    nums = [3,3,3,6,9,12]
    print(longestArithSeqLength2(nums))
