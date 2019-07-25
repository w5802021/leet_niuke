
def reverseStr(s, k):     ##########转换为列表操作###########
    l = list(s)
    for i in range(0, len(s), 2 * k):
        l[i:i + k] = reversed(l[i:i + k])
    return ''.join(l)

def reverseStr2(s, k):    ###########字符串操作###########
    res = ''
    for i in range(0, len(s), 2 * k):
        res += s[i:i + k][::-1] + s[i + k:i + 2 * k]

    return res

if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(reverseStr2(s,k))