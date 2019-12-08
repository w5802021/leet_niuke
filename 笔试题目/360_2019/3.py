q = int(input())

# 将十进制转换为k进制，k进制的每一位，用列表中的一个数表示，注意当k大于10时，k进制中的每一位可能为两位数
def dec2k(dec):
    ansk = []
    while dec:
        ansk.append(dec % k)
        dec = dec // k
    ansk = ansk[::-1]
    return ansk

# 将k进制转换为十进制，k进制的每一位，用列表中的一个数表示，注意当k大于10时，k进制中的每一位可能为两位数
def k2dec(rans):
    ansd = 0
    tmp = 1
    # 由低位加起
    for i in range(len(rans) - 1, -1, -1):
        ansd += rans[i] * tmp
        tmp *= k
    return ansd

# k进制表示中，k-1的数量最多的数，且输出最小的，即k进制数每一位均为k-1构成
def get_ans():
    if len(lvalue) == 0 or len(rvalue) == 0:
        return
    # 第一种全为(k-1), l <= and <= r
    record, tmp = 0, 0
    while tmp <= r:
        record = tmp
        tmp = tmp * k + (k - 1)
    # print("record:", record)
    if record >= l:
        return record

    else:
        # 每判断一下都需要进制转换，复杂度太高，超时，由于每次只更新一位，因此，可以直接修改
        # for i in range(len(lvalue) - 1, -1, -1):
        #     t = lvalue[i]
        #     lvalue[i] = k - 1
        #     if k2dec(lvalue) > r:  # 大于，则还原
        #         lvalue[i] = t
        #         return k2dec(lvalue)

        dec = k2dec(lvalue)
        tmp = 1
        for i in range(len(lvalue) - 1, -1, -1):
            dec = dec + (k - 1 - lvalue[i]) * tmp
            tmp = tmp * k
            t = lvalue[i]
            lvalue[i] = k - 1
            if dec > r:  # 大于，则还原
                lvalue[i] = t
                return k2dec(lvalue)

while q > 0:
    k, l, r = map(int, input().strip().split())
    lvalue = dec2k(l)
    rvalue = dec2k(r)
    print(get_ans())
    q -= 1




