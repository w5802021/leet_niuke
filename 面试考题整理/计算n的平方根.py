def squareroot(x):
    '''
    牛顿法   找到cur^2-x^2 = 0的函数 cur取何值时过零
    :param x:
    :param e:
    :return:
    '''
    if x <= 1:
        return x
    cur = x
    while cur*cur > x:
        cur = (cur + x/cur)//2

    return int(cur)

def squareroot1(x):
    '''
    二分法
    :param x:
    :param e:
    :return:
    '''

    low, high = 0, x // 2 + 1
    while low < high:
        mid = (low + high + 1) // 2
        if mid * mid > x:
            high = mid - 1
        else:
            low = mid
    return low