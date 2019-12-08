def isHappy(n):
    dic = set()
    m = n
    while True:
        summ = 0
        # 计算整数n各位数字的平方和
        while m != 0:
            summ += (m%10)**2
            m = m//10

        if summ == 1:
            return True
        elif summ in dic:
            return False
        else:
            dic.add(summ)
        m = summ

if __name__ == '__main__':
    n = 19
    print(isHappy(n))