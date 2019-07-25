def isSubsequence(s, t):
    count = 0
    if not s:
        return True
    for i in t:
        if s[count] == i:
            count += 1
            if count == len(s):
                return True
    return  False

def isSubsequence1(s, t):
    if not s:
        return True

    for ss in s:         ##遍历短串字符速度稍快
        res = t.find(ss)
        if res == -1:       #find()方法仅能用于字符串
            return False
        else:
            t = t[res+1:]
    return True


if __name__ == '__main__':
    s = "leeeeetcode"
    t = "yyyyylyyyyyyyyyyeyyyyyyyyyyyyyyeyyyyyyyyyyyyeyyyyyyyyyeyyyyyyyyyeyyyyyyyyyytyyyyyyyyyycyyyyyyyyyyyoyyyyyyyyyyyyydyyyyyyyyyyyeyyyyyyyyyyyy"
    print(isSubsequence1(s,t))