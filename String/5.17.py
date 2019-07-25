def getlargestsub(s):
    if s == None:
        return None
    s = list(s)
    n = len(s)
    largestsub = [None]*(n+1)
    largestsub[0] = s[n-1]
    j = 0                #代表上一个存入largestsub数组的数的下标

    for i in range(n-2,0,-1):
        if s[i] >= largestsub[j]:
            j += 1
            largestsub[j] = s[i]

    largestsub = largestsub[0:j+1]

    return ''.join(largestsub[::-1])

if __name__ == '__main__':
    s = 'acbdxmng'
    result = getlargestsub(s)
    print(result)
