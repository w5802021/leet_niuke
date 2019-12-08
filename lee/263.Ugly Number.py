def isUgly(num):
    '''
    判断是否为丑数
    丑数就是只包含质因数 2, 3, 5 的正整数。注意1也是丑数
    :param num:
    :return:
    '''
    if num == 0:
        return False
    while num != 1:
        if num % 2 == 0:
            num /= 2
        elif num % 3 == 0:
            num /= 3
        elif num % 5 == 0:
            num /= 5
        else:
            return False
    return True

if __name__ == '__main__':
    n = 14
    print(isUgly(n))