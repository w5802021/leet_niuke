def Add(num1, num2):

    while num2:
        # & 0xFFFFFFFF的作用是超过32位的越界处理 因为python数据结构会自动增位
        temp = (num1 ^ num2) & 0xFFFFFFFF
        num2 = ((num1 & num2) << 1) & 0xFFFFFFFF
        num1 = temp
    # <= 0x7FFFFFFF表示是正数   ~(num1 ^ 0xFFFFFFFF) 表示负数的补码 ~n = -(n+1)
    return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)