def getmaxdupstr(s):  #迭代法
    maxlen = 0
    curmaxlen = 0
    prechar = ''
    for i in s:
        if i != prechar:
            maxlen = max(maxlen,curmaxlen)
            curmaxlen = 1
            prechar = i
        else:
            curmaxlen += 1
    return maxlen

def getmaxdupstr1(s,index,curmaxlen,maxlen):  #递归法
    if index == len(s) - 1:
        return max(maxlen,curmaxlen)

    if s[index] == s[index-1]:
        curmaxlen += 1
        return getmaxdupstr1(s, index + 1, curmaxlen, maxlen)
    else:
        maxlen = max(maxlen,curmaxlen)
        curmaxlen = 1
        return getmaxdupstr1(s,index+1,curmaxlen,maxlen)

if __name__ == '__main__':
    s = 'abcabcbb'
    # print(getmaxdupstr(s))
    print(getmaxdupstr1(s,0,1,1))
