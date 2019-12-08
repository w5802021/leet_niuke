def deal(n, l):
    return sum(l[0:n:2]) - sum(l[1:n:2])

if __name__ == '__main__':
    n = 3
    l = [2,7,4]
    l.sort()
    l = l[::-1]
    print(deal(n, l))

