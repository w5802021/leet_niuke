k = int(input().strip())
a, x, b, y = list(map(int, input().split()))

mod = 1000000007
# dp[i]表示总歌单长度为i时，一共有多少组组成歌单的方法
dp = [0] * (k+1)
dp[0] = 1
#在x首长度为A的歌中选，总歌单长度i的歌单组成方法
for i in range(1, x + 1):
    for j in range(k, a - 1, -1):
        dp[j] = dp[j] + dp[j-a]
#在y首长度为B的歌中选，总歌单长度i的歌单组成方法
for i in range(1, y + 1):
    for j in range(k, b - 1, -1):
        dp[j] = dp[j] + dp[j - b]
print(dp[k])