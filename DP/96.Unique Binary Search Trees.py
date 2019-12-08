def numTrees(n):
    '''
    动态规划方法
    思路：假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
            G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
         当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
            f(i) = G(i-1)*G(n-i)
         从而得
            G(n)=G(0)∗G(n−1)+G(1)∗G(n−2)+...+G(n−1)∗G(0)  (n从1开始)   当n=0时， G(0) = 1
    :param n:
    :return:
    '''
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            # dp[i-1-j]代表最后取到的i-1
            dp[i] += dp[j] * dp[i-1-j]
    return dp[-1]

def numTrees1(n):
    '''
     思路:由上面公式，根据数学归纳法, 可直接得到, G(0) = 1, G(n+1) = 2*(2*n+1)*G(n)/(n+2)   这样的公式称为卡特兰数
    :param n:
    :return:
    '''
    C = 1
    for i in range(0,n):
        C = 2*(2*i+1)*C//(i+2)
    return C

if __name__ == '__main__':
    n = 12
    print(numTrees(n))