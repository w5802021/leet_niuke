
n = int(input())
m = int(input())
for _ in range(n):
    graph = []
    for mm in range(m):
        a = [int(c) for c in input().split()]
        featnum = a[0]
        ff = []
        for i in range(featnum):
            ff.append((a[2*i+1],a[2*i+2]))
        graph.append(ff)

    cnts = {}
    for frame in range(m):
        for feat in graph[frame]:
            tmp = frame
            count = 1
            while tmp+1 <= m-1 and feat in graph[tmp+1]:
                count += 1
                tmp += 1
            if feat not in cnts:
                cnts[feat] = count
            elif count > cnts[feat]:
                cnts[feat] = count

    res = float('-inf')
    for i in cnts:
        if cnts[i] > res:
            res = cnts[i]
    print(res)




