
def deal(n, ll, a, b, k):

    t = int(k - ll[a][b])
    if t < 0:
        return 0
    else:
        return t

if __name__ == "__main__":

    n = 3
    ll = [[0, 2, 3],[2, 0, 5],[3, 5, 0]]
    a, b, k = 1,2,3
    print(deal(n, ll, a, b, k))


