def LeftRotateString(s, n):
    '''
    复制字符串，切片
    :param s:
    :param n:
    :return:
    '''
    leng = len(s)
    if leng == 0:
        return ""
    n = n % leng
    s += s
    return s[n:n + leng]

def LeftRotateString1(s, n):
    '''
    双旋转  YX = （X^T  Y^T）^T
    :param s:
    :param n:
    :return:
    '''
    if len(s) == 0:
        return ""
    s = s[::-1]
    n = n % len(s)
    s1 = s[:len(s)-n]
    s2 = s[len(s)-n:]
    return s1+s2
