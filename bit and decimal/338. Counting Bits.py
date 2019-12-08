def countBits(num):
    '''
    判断二进制数有多少个1
     动态规划
    :param num:
    :return:
    '''
    dp = [0] * (num + 1)
    for i in range(num + 1):
        # dp[i] = dp[i/2] + (i % 2)
        dp[i] = dp[i >> 1] + (i % 2)
    return dp

def countBits1(num):
    '''
    判断二进制数有多少个0
     动态规划
    :param num:
    :return:
    '''
    dp = [0] * (num + 1)
    dp[0] = 1
    dp[1] = 0
    for i in range(2,num + 1):
        # dp[i] = dp[i/2] + (i % 2)
        dp[i] = dp[i >> 1] + ((i+1) % 2)
    return dp


if __name__ == '__main__':

    num = 10
    print(countBits1(num))