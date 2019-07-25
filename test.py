def sqrt_doubleqplit(num):
    low = 0
    high = num
    for i in range(1000):
        mid = low + (high - low)/2
        if pow(mid,2) > num:
            high =  mid
        elif pow(mid,2) < num :
            low =  mid
    return low

if __name__ == '__main__':
    a = 2**32
    print(sqrt_doubleqplit(a))

