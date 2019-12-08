def countbit(n):
    count = 0
    if n < 0:
        # 对负数取补码
        n = n & 0xffffffff

    while n:
        count += 1
        # 避免负数移位造成最高位的补充位都是1的影响 (对负数移位，最左边的用1填充)   -->  这里是将最右边的1变为0
        # x = bin(n)
        n = (n-1) & n
        # y = bin(n)
        a = 1
    return count

if __name__ == '__main__':
    n = -15
    print(countbit(n))
    # -15的补码为（保持符号位不变，其他位按位取反再+1）    1111 1111 1111 1111 1111 1111 1111 0001