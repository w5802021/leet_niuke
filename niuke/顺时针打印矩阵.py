def spiralOrder(matrix):
    u = 0
    d = len(matrix) - 1
    l = 0
    r = len(matrix[0]) - 1
    res = []
    while True:
        for i in range(l,r+1):
            res.append(matrix[u][i])
        u += 1
        if u > d:break

        for i in range(u,d+1):
            res.append(matrix[i][r])
        r -= 1
        if r < l:break

        for i in range(r,l-1,-1):
            res.append(matrix[d][i])
        d -= 1
        if d < u:break

        for i in range(d,u-1,-1):
            res.append(matrix[i][l])
        l += 1
        if l > r:break
    return res
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(spiralOrder(matrix))
