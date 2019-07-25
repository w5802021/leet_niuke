class jumpfl():


    def jumpFloor(self,number):          #跳台阶问题，一次可以跳1,2中的数
        # write code here
        dp = [0] * number

        if number <= 1:
            dp[0] = 1
        else:
            dp[0] = 1                    #斐波那契数列法
            dp[1] = 2
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[len(dp) - 1]


    def jumpFloorII(self,number):           #变态跳台阶问题，一次可以跳1，2，...,n中的任意的数
            # n = number
            # n = 1, f(1) = 1
            # n = 2, f(2) = f(2-1) + f(2-2)  第一步跳了一个台阶后面还能有多少种跳法 + 第二步跳了二个台阶后面还能有多少种跳法
            # ...
            # f(n-1) = f(n-2) + f(n-2) + ... + f(0)
            # f(n) = f(n-1) + f(n-2) + ... + f(0) = 2 * f(n-1)
            # 数学归纳法的思想推导求得迭代公式  f(n) = 2 * f(n-1)

            if number == 1:
                return 1
            else:
                return 2 * self.jumpFloorII(number - 1)

if __name__ == '__main__':
    setl = jumpfl()
    print(setl.jumpFloor(569))
    print(setl.jumpFloorII(569))
