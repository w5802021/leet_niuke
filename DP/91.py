def numDecodings(s):
    '''
    序列型动态规划
    :param s:
    :return:
    '''
    nums = list(s)
    n = len(s)
    if n == 0:
        return 0
    # dp[i]表示(s[0:i-1)个字符的解码方法
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        t = ord(nums[i - 1]) - ord('0')
        # 判断一位字符串解码方式
        if (t >= 1 and t <= 9):
            dp[i] += dp[i - 1]
        # 判断两位的字符串解码方式
        if i >= 2:
            t = (ord(nums[i - 2]) - ord('0')) * 10 + (ord(nums[i - 1]) - ord('0'))
            if t >= 10 and t <= 26:
                dp[i] += dp[i - 2]
    return dp[n]

#################################639#######################################
def numDecodings1(s):
    '''
    序列型动态规划
    :param s:
    :return:
    '''
    nums = list(s)
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    mod = 1000000007
    for i in range(1, n + 1):
        if s[i - 1] == '*':
            dp[i] = (dp[i] + 9 * dp[i - 1]) % mod
            if i >= 2:
                if s[i - 2] == '*':
                    dp[i] = (dp[i] + 15 * dp[i - 2]) % mod
                elif s[i - 2] == '1':
                    dp[i] = (dp[i] + 9 * dp[i - 2]) % mod
                elif s[i - 2] == '2':
                    dp[i] = (dp[i] + 6 * dp[i - 2]) % mod
        else:
            if s[i - 1] >= '1' and s[i - 1] <= '9':
                dp[i] = (dp[i] + dp[i - 1]) % mod
            if i >= 2:
                if s[i - 2] == '*':
                    if s[i - 1] >= '0' and s[i - 1] <= '6':
                        dp[i] = (dp[i] + 2 * dp[i - 2]) % mod
                    elif s[i - 1] >= '7' and s[i - 1] <= '9':
                        dp[i] = (dp[i] + dp[i - 2]) % mod
                else:
                    twoDigits = int(s[i - 2: i])
                    if twoDigits >= 10 and twoDigits <= 26:
                        dp[i] = (dp[i] + dp[i - 2]) % mod
    return dp[n]

if __name__ == '__main__':
    s = "*1*1*0"
    print(numDecodings1(s))
