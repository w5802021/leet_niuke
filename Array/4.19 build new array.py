def cacu(a,b):
    b[0] = 1
    N = len(b)
    for i in range(1,N):
        b[i] = b[i-1] * a[i-1]

    b[0] = a[N-1]

    for i in range(N-2,0,-1):
        b[i] *= b[0]
        b[0] *= a[i]

    return b

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    b = [None]*len(a)
    print(cacu(a,b))

