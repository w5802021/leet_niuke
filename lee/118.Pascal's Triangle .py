
def generate(numRows):   #自己的方法
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]

    res = [[1], [1, 1]]

    for i in range(2, numRows):
        col = i + 1
        dp = []
        for j in range(col):
            if (j == 0) | (j == (col - 1)):
                dp.append(1)

            else:
                dp.append(res[i - 1][j - 1] + res[i - 1][j])
        res.append(dp)
    return res

def generate2(numRows):     #标准答案

    res = []

    for i in range(numRows):
        col = i + 1
        dp = [None for _ in range(col)]
        dp[0] = 1
        dp[-1] = 1

        for j in range(1,col-1):

            dp[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(dp)
    return res

def getRow(rowIndex):                         ############119###########优化空间复杂度
        dp = []
        for i in range(rowIndex):

            col = i + 1
            dp = dp + [None]
            dp[0] = 1
            dp[-1] = 1
            pt = 1
            for j in range(1, col - 1):
                dp[j], pt = pt + dp[j], dp[j]

        return dp

if __name__ == '__main__':
    n = 5
    print(generate(n))
    print(getRow(5))