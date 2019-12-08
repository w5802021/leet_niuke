m = int(input())
S = input().split()

def numPermsDISequence(S):

    mod = 10 ** 9 + 7
    n = len(S)
    # dp[i][j]代表符合01规则的前i个位置的由j结尾的数组的数目，那么可以求得递推公式：
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            # 当S[i - 1]为0时，p[i-1] < p[i]
            if S[i - 1] == '1':
                # dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + ... + dp[i-1][i-1]
                for k in range(j, i):
                    # here start from j, regard as swap value j with i, then shift all values no larger than j
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod
            else:
                # dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j-1]
                for k in range(0, j):
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod
    # print(dp)
    return sum(dp[n]) % mod

print(numPermsDISequence(S))

