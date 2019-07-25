def minDeletionSize( A):
    res = 0
    for i in range(len(A[0])):
        for j in range(1, len(A)):
            a = A[j][i]
            b = A[j-1][i]
            if A[j][i] < A[j - 1][i]:
                res += 1
                break
    return res

def minDeletionSize1( A):
    res = 0
    for i in zip(*A):
        if list(i) != sorted(i):
            res += 1
    return res

if __name__ == '__main__':
    A = ["zyx","wvu","tsr"]
    print(minDeletionSize1(A))