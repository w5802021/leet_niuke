def factor(x):
    total = 0
    for i in range(1,x+1):
        if x%i == 0:
            total += 1
    # x若为奇数个约数，则为最后亮的灯
    return 1 if total % 2 == 1 else 0

def totallight(num,n):
    count = 0
    res = []
    for i in range(n):
        if factor(num[i]) == 1:
            count += 1
            res.append(num[i])
    return res,count

if __name__ == '__main__':
    n = 100
    num = [0] * n
    for i in range(n):
        num[i] = i+1
    print(totallight(num,n))