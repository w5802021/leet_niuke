# python3
def main():
    case = int(input())
    for t in range(case):
        n = int(input())
        golds = [int(c) for c in input().split()]
        # dp[i][j]表示在golds[i-1:j]中博弈时，先手方最多能拿到多少价值
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        sum = [0 for _ in range(n + 1)]
        #初始化
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + golds[i - 1]
            dp[i][i] = golds[i - 1]

        for j in range(n):
            for i in range(1, n):
                if i + j <= n:
                    # i+j为序列右边边界
                    # min(dp[i + 1][i + j], dp[i][i + j - 1])最小化对手价值
                    # sum[i + j] - sum[i - 1] 为sum(golds[i-1:i+j])
                    dp[i][i + j] = sum[i + j] - sum[i - 1] - min(dp[i + 1][i + j], dp[i][i + j - 1])
        print ('Case #%d: %d %d'%(t + 1, dp[1][n], sum[n] - dp[1][n]))

if __name__ == '__main__':
    main()




