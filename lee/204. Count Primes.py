
def countPrimes(n):
    '''
    统计所有小于非负整数 n 的质数的数量
    方法
    :param n:
    :return:
    '''
    if n < 3:
        return 0
    res = [1] * n
    res[0],res[1]=0,0
    # i*i--n--步进位i   【int(n**0.5)】*【int(n**0.5)】
    for i in range(2,int(n**0.5)+1):
        # 将是output[i]倍数的数都化为0
        if res[i] == 1:
            res[i**2:n:i] = [0] * len(res[i**2:n:i])
    return sum(res)

if __name__ == '__main__':
    n = 10
    print(countPrimes(n))

