def wordBreak(s, wordDict):
    ####该方法存在问题，若存在复杂子问题时，要想到DP
    for i, w in enumerate(wordDict):
        while s.find(w) != -1:
            s = s[:s.find(w)] + s[s.find(w) + len(w):]

    return True if len(s) == 0 else False

def wordBreak1(s, wordDict):
    dp = [True]
    for i in range(1, len(s) + 1):
        # dp[j] s[j:i] + for循环迭代器 判断是否在单词表里
        # 用动态，前面已经判断能用单词表组成的字符串在下一次就不需要在判断了（这里any()函数相当于or，具有短路功能，all()相当于and）
        dp.append(any(dp[j] and s[j:i] in wordDict for j in range(i)))
    return dp[-1]

def wordBreak2(s, words):
    dp = [True]
    # 优化  使用最长单词的长度做限定  加['']防止给的wordict 为空
    max_len = max(map(len,words+['']))
    words = set(words)
    for i in range(1, len(s)+1):
        dp += any(dp[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
    return dp[-1]

def wordBreak3(s, wordDict):       ####清晰版
    '''
    题意：给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
         拆分时可以重复使用字典中的单词
         你可以假设字典中没有重复的单词
    :param s:
    :param wordDict:
    :return:
    '''
    # 集合去重
    wordDict = set(wordDict)
    # 1、确定状态,dp[i]表示字符串s[0：i]是否能由worddict中的单词拆分
    # 3、初始化及边界条件
    dp = [True] + [False] * (len(s))
    max_len = 0
    # 求出worddict中最长单词的长度
    for word in wordDict:
        max_len = max(max_len, len(word))
    # 4、计算顺序 自左往右
    for i in range(1, len(s) + 1):
        # 这里对DP数组递推过程的第二维遍历过程进行优化，
        # 每次遍历只是从worddict中找到一个单词使得其到达dp[i]
        # 这样第二维的遍历长度降为定值max_len，
        for k in range(max(i - max_len, 0), i):
            # 2、递推公式 bool型（存在型）递推公式
            if dp[k] and s[k:i] in wordDict:
                dp[i] = True
    return dp[len(s)]

############################引申题5.13##################################
list = ['test','tester','testertest','testing','apple','seattle','banana','batting','ngcat','batti','bat',
        'testingtester','testbattingcat']

def findlongestword(nums):
    '''
    题意：找出list表中的字符串能由数组中其它字符串组成的最长字符串
    方法：采用贪心算法，对list列表按长度进行排序，遍历列表直到找到一个字符串满足题意，输出的就是最长的字符串
    '''
    nums.sort(key=len,reverse=True)
    for i in nums:
        num_ex = nums.copy()
        del num_ex[nums.index(i)]
        if wordBreak3(i,num_ex):
            return i

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet","code"]
    # print(findlongestword(list))
    print(wordBreak3(s,wordDict))