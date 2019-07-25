
def longestPalindrome(s):
    dic = {}
    res = 0

    odds = False   #记录是否有奇数个的相同字符

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    if len(dic) == 1:       #字符串都相同
        return dic[s[0]]

    for j in dic:
        if dic[j] % 2 == 0:
            res += dic[j]
        else:
            res += dic[j] - 1
            odds = True

    if odds:               #存在奇数个的字符的情况，要记得加1，因为最后只能保留一个是奇数的字符
        res += 1
    return res

if __name__ == '__main__':
    nums = "tattarrattat"
    print(longestPalindrome(nums))