import random
def getmaxmoney(n):
    '''

    :param n:房间的数量
    :return:
    '''

    a = [None] * n
    for i in range(n):
        a[i] = random.uniform(1,n)
    # 前4个房间中最多金币的量
    max4 = 0
    for i in range(4):
        if a[i] > max4:
            max4 = a[i]
    for i in range(4,n-1):
        if a[i] > max4:
            return True if a[i] == max(a) else False
    # for i in range(4,n-1):
    #     if a[i] > max4:
    #         return True
    return False

if __name__ == '__main__':
    n = 10
    test_n = 100000
    success = 0
    for i in range(test_n):
        if getmaxmoney(n):
            success += 1
    print(success/test_n)
