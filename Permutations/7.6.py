def comb(n):
    count = 0
    for m in range(0,n+1,5):
        count += (m+2)//2
    return count

if __name__ == '__main__':
    n = 100
    print(comb(n))
