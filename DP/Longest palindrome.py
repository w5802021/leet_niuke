
#Q:给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
#输出需要删除的字符个数。


#区分最长公共子序列与最长子串的区别

#最长公共子序列：要求可以不连续

#最长公共子串：公共子串必须在原串中是连续的

#最长回文串：其正序串S与逆序串S'的最长公共子串不一定就是最长回文串；还需要注意当我们找到最长的公共子串
#的候选项时，都需要检查子串的索引是否与反向子串的原始索引相同。如果相同，那么我们尝试更新目前为止找到的最长回文子串；
#如果不是，我们就跳过这个候选项并继续寻找下一个候选。

class DP:
    # 最大公共子序列
    def maxlcs(self,a,b):

        m = len(a)
        n = len(b)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        mem = [[None for i in range(n+1)] for j in range(m+1)]
        res = []

        for i in range(1,m+1):
            for j in range(1,n+1):

                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    mem[i][j] = 'ok'

                elif dp[i-1][j] >= dp[i][j-1]:    #这里注意符号一定是大于等于
                    dp[i][j] = dp[i-1][j]
                    mem[i][j] = 'up'

                else:
                    dp[i][j] = dp[i][j - 1]
                    mem[i][j] = 'left'

        p1,p2 = m,n
        while dp[p1][p2]:
            cc = mem[p1][p2]
            if cc == 'ok':
                res.append(a[p1-1])
                p1-=1
                p2-=1
            if cc == 'left':
                p2-=1
            if cc == 'up':
                p1 -= 1
        res = ''.join(res[::-1])
        return res,dp[m][n]

    # 最长公共子串
    def maxlss(self,a,b):
        '''
        思路
        '''
        m = len(a)
        n = len(b)
        # dp[i][j]表示a的子串a[:i]与b的子串b[:j]的最长公共子串的长度
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        result = 0
        # a序列最长子串最后的索引位置
        last = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > result:
                        result = dp[i][j]
                        last = i
                else:
                    dp[i][j] = 0

        return a[last-result:last],result

    def longestPalindrome(self, s):
        #DP的方法 但是速度较慢 待优化
        if not s:
            return ''
            # 先将任一单个字母作为结果
        start = 0
        maxlen = 1
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # 将长度1和长度2（相同字母）情况初始化赋值
        for i in range(len(s)):
            dp[i][i] = 1
            if (i < len(s) - 1) and (s[i] == s[i + 1]):     #找到两个字母的回文
                dp[i][i + 1] = 1
                start = i
                maxlen = 2
        # 注意：不可横向遍历，否则例如abcba，是无法先将bcb置为1的，进而无法将abcba置为1

        for length in range(3, len(s) + 1):   #找到length个字母的回文 从3开始  因为初始化时已经找到两个字母的回文
            for i in range(len(s) - length + 1):
                j = i + length - 1   #i是回文串的tou j是回文串的尾
                if (dp[i + 1][j - 1] == 1) and s[i] == s[j]:
                    dp[i][j] = 1
                    if length > maxlen:
                        start = i
                        maxlen = length
        # for line in dp:
        #     print line
        return s[start:start + maxlen]

##############################中心拓展法#########################################
    def longestPalindrome2(self, s):      #最长回文串   如何用动态规划求解

        res = ''
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)   # i,i即代表找最大回文数是奇数情况的
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)   # i,i+1即代表找最大回文数是偶数情况的，
            if len(tmp) > len(res):
                res = tmp
        return res

        # get the longest palindrome, l, r are the middle indexes
        # from inner to outer

    def helper(self, s, l, r):
        while 0 <= r < len(s) and s[l] == s[r]:  # 从中间开始往两边检测最长回文数
            l -= 1
            r += 1
        return s[l + 1:r]

    #动态规划求解
    def longestPalindrome3(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        dp = [[0 for _ in range(size)] for _ in range(size)]
        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，l+1<=r-1 如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # a1 or a2 满足a1就不会在判断a2
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
        return res

if __name__ ==  '__main__':
    mal = DP()
    print(mal.maxlcs(['A','B','C','B','D','A','B'],['B','D','C','A','B','A']))
    print(mal.maxlss("babad", 'dabab'))
    print(mal.longestPalindrome3('google”'))