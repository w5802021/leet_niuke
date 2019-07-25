def minDistance(word1, word2):
    '''
    题意：给定两个单词word1 = "horse", word2 = "ros"，只能使用三种操作：插入、删除、替换，每种操作计数1次，
         问需要多少次操作使word1转换为word2
    思路：迭代动态规划
         1、自顶向下
         2、dp[i][j]代表word1(0至i-1)位置上的字符转换为word2（0至j-1）位置上的字符需要多少次操作
    '''

    n1 = len(word1)
    n2 = len(word2)
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    # 边界处理
    for i in range(n1+1):dp[i][0] += i
    for j in range(n2+1):dp[0][j] += j
    # 动态规划
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            # 如果两个单词当前最后位置上的元素相同
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # [i-1][j]代表删除操作，[i][j-1]代表插入操作，[i-1][j-1]替换操作
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
    return dp[-1][-1]

def minDistance1(word1, word2):
    '''
    思路：递归动态规划
          速度更快
    '''
    dp = [{} for _ in range(len(word1) + 1)]

    def getDistance(i, j):
        # 边界处理
        if i == 0: return j
        if j == 0: return i
        # 优化点，递归时不需要计算所有dp矩阵位置的值，根据条件筛选后，减少了许多计算量
        if j in dp[i]: return dp[i][j]
        #
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = getDistance(i - 1, j - 1)
        else:
            dp[i][j] = min(getDistance(i - 1, j - 1),getDistance(i - 1, j),getDistance(i, j - 1)) + 1
        return dp[i][j]
    res = getDistance(len(word1), len(word2))
    return res

if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    print(minDistance1(word1,word2))