def deal(n, h, ll):

    for i in range(1,len(ll)+1):
        sum = []
        for j in range(1,i):
            if ll[j-1] >= h - (h-ll[i-1])*j/i:
                sum.append(j)
        if sum == []:
            print(0)
        else:
            print(max(sum))

if __name__ == "__main__":
    # s = input().split()
    n = 9
    h = 5
    ll = [5,4,3,4,3,3,3,3,3]
    deal(n, h, ll)