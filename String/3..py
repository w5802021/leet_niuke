'''
方法一：暴力法
'''
def lengthOfLongestSubstring(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if allunique(s,i,j):
                res = max(res,j-i)

    return res
def allunique(s,st,end):
    uni = []
    for i in range(st,end):
        if s[i] in uni:
            return False
        uni.append(s[i])
    return True

'''
方法二：滑动窗口法  (类似队列)
'''

def lengthOfLongestSubstring1(s):
    n = len(s)
    uni = []
    res = 0
    i,j = 0,0
    while i < n and j < n:
        if s[j] not in uni:
            uni.append(s[j])
            j += 1
            res = max(res,j-i)
        else:
            uni.remove(s[i])
            i += 1
    return res

'''
方法三：优化的滑动窗口法 substr即为窗
'''

def lengthOfLongestSubstring2(s):
    '''
    substr:即为输出的无重复字符的最长子串
    '''
    substr = ''
    maxlen = 0

    for char in s:
        if char not in substr:
            substr += char
            maxlen = max(maxlen, len(substr))
        else:
            substr = substr[substr.index(char) + 1:] + char

    return maxlen

if __name__ == '__main__':
    s = 'pwwkew'
    print(lengthOfLongestSubstring2(s))