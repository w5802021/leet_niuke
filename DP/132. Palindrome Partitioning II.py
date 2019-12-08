###################################131####################################
def partition(s: str):
    '''
    dfs 回朔法
    :param s:
    :return:
    '''
    def dfs(s, tmp, res):
        if not s:
            res.append(tmp)
            return 0
        for i in range(len(s)):
            if s[:i + 1] == s[i::-1]:
                dfs(s[i + 1:], tmp + [s[:i + 1]], res)

    res = []
    tmp = []
    dfs(s, tmp, res)
    return res

################################132################################
def minCut( s):
    '''
    动态规划 + 中心拓展
    :param s:
    :return:
    '''
    n = len(s)
    # 记录字符串s[l:r+1]是否为回文串
    ispalin = [[False] * n for _ in range(n)]
    for i in range(n):
        # odd case, like "aba"
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ispalin[l][r] = True
            l -= 1
            r += 1
            # even case, like "abba"
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ispalin[l][r] = True
            l -= 1
            r += 1
    # 状态dp[i]为  s[0:i-1]子串最少可以划分为多少个回文串
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if ispalin[j][i - 1]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n] - 1

if __name__ == '__main__':
    s = 'aab'
    print(minCut(s))