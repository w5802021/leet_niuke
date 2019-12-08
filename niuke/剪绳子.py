class Solution:
    def cutRope(self, number):
        '''
        贪心解法
        '''
        num = number
        if num == 2:
            return 1
        elif num == 3:
            return 2
        mod = num % 3
        zhen = num // 3
        if mod == 0:
            return pow(3, zhen)
        elif mod == 1:
            return 2 * 2 * pow(3, zhen - 1)
        else:
            return 2 * pow(3, zhen)

    def cutRope1(self, number):
        '''
        动态规划解法
        '''
        if number < 2:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2

        dp = [0 for _ in range(number + 1)]

        dp = [0 for _ in range(number + 1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4,number + 1):
            for j in range(1,(number//2)+1):
                dp[i] = max(dp[i],dp[j]*dp[i-j])

        return dp[number]


test = Solution()
print(test.cutRope1(4))