def convertToBase7(num: int) -> str:
    res = []
    # 十进制转k进制处理方法
    if num > 0:
        while num:
            res.append(num % 7)
            num //= 7
        res = res[::-1]
        return ''.join(str(c) for c in res)
    elif num < 0:
        num = abs(num)
        while num :
            res.append(num % 7)
            num //= 7
        res = res[::-1]
        return '-' + ''.join(str(c) for c in res)
    else:
        return '0'

print(convertToBase7(-7))