def schedule(R,O,n,m):

    def sort_val(R,O):
        for i in range(n):
            for j in range(i+1,n):
                if R[j] - O[j] > R[i] - O[i]:
                    R[i],R[j] = R[j],R[i]
                    O[i], O[j] = O[j], O[i]

    sort_val(R,O)
    remain = m
    for i in range(n):
        if remain < R[i]:
            return False
        else:
            remain -= O[i]
    return True

if __name__ == '__main__':
    R = [10,15,23,20,6,9,7,16,50]
    O = [2,7,8,4,5,8,6,8,10]
    m = 50
    n = 9
    print(schedule(R,O,n,m))



