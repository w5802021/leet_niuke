n = 1000
nums = '4 7 5 3 4 5 6 2 1 6 8 8 2 8 7 7 1 7 2 2 6 8 6 7 5 1 6 6 1 7 6 1 1 7 7 3 1 1 5 6 4 2 8 8 1 1 8 6 4 4 4 4 6 4 5 3 7 7 6 4 3 4 7 5 3 4 3 1 6 7 6 4 7 4 3 8 1 6 4 1 8 3 3 8 2 6 2 6 6 8 6 7 3 2 1 1 4 6 7 5 2 7 1 5 3 6 1 7 2 6 5 1 7 3 7 5 1 6 4 7 8 4 4 5 8 8 2 6 3 5 4 6 6 1 5 1 7 7 1 5 5 3 1 5 8 3 8 4 3 4 4 7 8 3 1 6 2 6 3 4 8 1 2 4 1 5 3 7 3 6 5 3 1 4 1 6 4 5 5 4 8 8 2 5 3 5 5 3 2 4 3 2 4 3 1 8 3 3 3 7 8 5 3 1 6 1 4 4 2 8 7 6 1 3 6 2 3 2 8 3 6 2 4 1 6 1 1 2 4 4 5 3 5 3 4 7 4 2 4 6 2 4 6 2 5 3 8 6 7 3 1 8 1 8 4 8 7 4 1 1 5 6 8 8 2 8 8 3 4 7 7 5 5 8 2 7 4 1 7 8 7 6 1 7 8 6 4 8 5 5 2 6 5 2 6 1 7 4 6 8 5 8 6 8 2 6 3 5 7 6 5 8 4 5 8 3 5 4 4 1 2 2 4 1 4 1 5 4 5 7 8 4 8 6 1 8 1 5 8 5 5 8 8 8 5 6 6 1 7 2 4 2 6 5 7 1 3 1 6 1 3 1 4 8 3 7 8 4 2 5 2 7 6 1 1 5 2 3 3 4 6 8 4 3 7 4 3 6 1 4 1 1 2 2 3 3 8 4 2 5 6 7 2 2 3 7 7 2 4 3 7 2 3 7 3 6 7 1 7 1 6 8 5 4 1 2 5 5 7 6 1 2 4 1 5 7 3 4 4 4 2 5 1 3 5 5 3 8 6 3 5 2 3 7 4 1 8 1 2 8 7 3 3 4 5 4 6 6 6 7 6 6 4 3 2 8 4 4 2 4 2 2 3 8 7 8 4 1 7 8 2 2 8 4 1 3 7 8 4 6 5 7 6 6 2 4 2 1 1 2 1 8 5 5 2 4 2 3 6 3 7 5 4 3 2 2 2 6 4 6 6 7 7 6 4 4 5 8 1 5 3 1 7 4 6 6 1 5 4 7 2 8 7 1 1 4 5 4 8 6 4 4 5 2 4 3 8 2 5 7 6 5 2 8 6 1 6 4 2 4 6 6 8 7 7 5 1 4 2 1 1 2 5 4 1 7 5 6 2 5 8 1 3 8 7 6 4 7 3 7 3 8 8 7 7 1 8 7 4 4 1 3 7 3 1 4 2 5 8 7 1 7 8 6 6 7 1 5 2 5 8 8 5 2 8 2 1 5 1 1 2 4 8 1 8 8 8 6 7 5 7 6 6 8 4 6 8 1 8 4 8 3 2 5 8 2 8 8 4 5 2 2 2 3 1 3 5 2 8 1 2 6 2 3 2 8 4 1 1 7 4 3 6 3 3 7 4 7 7 7 1 6 4 2 5 2 3 1 5 1 3 4 1 1 8 7 2 5 1 8 8 1 6 2 3 2 2 6 1 2 5 8 7 2 6 8 3 8 7 3 2 4 8 1 5 6 1 8 1 2 2 1 7 6 5 1 1 3 7 3 6 2 3 3 8 1 8 6 4 6 4 1 2 4 8 7 6 4 5 7 6 5 7 5 4 7 2 8 6 4 3 4 4 8 8 1 2 2 2 3 8 4 2 3 6 8 2 6 3 3 5 5 8 7 1 5 8 3 4 7 3 5 5 3 4 3 4 8 7 6 5 7 6 1 1 1 6 1 6 6 6 4 8 8 8 7 7 7 3 3 3 6 8 7 5 6 3 4 8 2 5 5 8 2 8 5 2 3 2 6 4 7 5 7 6 2 6 6 1 5 5 6 7 6 4 2 4 7 4 3 3 5 4 6 4 4 4 2 4 2 1 8 5 1 1 3 8 1 2 3 8 6 5 5 1 5 1 5 1 4 6 7 5 3 6 1 7 6 3 5 7 4 5 6 8 5 2 1 5 7 3 7 3 1 5 7 8 4 5 1 4 7 8 8 7 2 2 8 4 6 4 1 4 3 4 1 6 1 8 1 5 3 2 1 2 8 3 6 4 4 1 5 6 7 3 8 8 4 7 8'
# n = int(input())
nums = [int(c) for c in nums.split()]

def main(n,nums):
    idx = [0]
    dic = set()
    mod = 1000000007

    if len(set(nums)) == n:
        return str(2**(n - 1))

    for i in range(len(nums)):

        if nums[i] not in dic:
            dic.add(nums[i])
        else:
            dic.clear()
            idx.append(i)

    res = 0
    for j in range(len(idx)-1):

        arr = nums[idx[j]:idx[j+1]]

        res += 2**(len(arr) - 1)
    res = res%mod
    return res

def main1(n,bal):
    '''
    动态规划（划分型动态规划）
    :param n:
    :param bal:
    :return:
    '''
    # dp[i]表示对于序列bal[:i]可以有多少种分法
    # 比如第i+1个数可以单独一组或者和第i、i-1个数组成一组，但不能和第i-2个数分到一组，那么dp[i+1]=dp[i]+dp[i-1]+dp[i-2]
    # 固定bal[i]为一组，则由dp[i]种方式，固定bal[i-1]、bal[i]为一组，则有dp[i-1]种方式，
    # 固定bal[i-2]、bal[i-1]、bal[i]为一组，则有dp[i-2]种方式
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n):
        # dp[i+1] += dp[i]
        j = i-1
        col = set()
        col.add(bal[i])
        # j代表当前位置i前面的位置
        while j >= 0:
            # 若在前面的串出现重复数字，则不要继续往前搜索
            if bal[j] in col:
                break
            col.add(bal[j])
            # dp[i+1] += dp[j]
            j -= 1
        dp[i + 1] = sum(dp[j+1:i + 1])
    return dp[n] % 1000000007

if __name__ == '__main__':
    print(main1(n, nums))


