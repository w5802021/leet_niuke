def isPowerOfTwo(n):
    '''
    思路:常规迭代
    '''
    if n == 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

def isPowerOfTwo1(n):
    '''
    思路:由于是2的幂次方，n的二进制表示形式都是类10000...的形式，即1总是只出现在最高位
    '''
    return n > 0 and n & (n - 1) == 0

if __name__ == '__main__':
    print(isPowerOfTwo(3))