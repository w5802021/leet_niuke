def countDigitOne(n):
    '''
    思路：
    :param n:
    :return:
    '''
    cnt, i = 0, 1
    while i <= n:  # i 依次个、十、百...位的算，直到大于 n 为止。
        cnt += n // (i * 10) * i + min(max(n % (i * 10) - i + 1, 0), i)
        i *= 10
    return cnt

if __name__ == '__main__':
    n = 100
    print(countDigitOne(n))


