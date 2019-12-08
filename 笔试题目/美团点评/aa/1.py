grid = input()
points = input()

A = []
tmp = []
for i in grid:
    if i == '0' or i == '1':
        tmp.append(int(i))
    if len(tmp) == 4:
        A.append(tmp)
        tmp = []

B = []
tp = []
for i in points:
    if i != '[' and i != ']' and i != ',':
        tp.append(int(i))
    if len(tp) == 2:
        B.append(tp)
        tp = []

# A = [[0,0,1,1],[1,0,1,0],[0,1,1,0],[0,0,1,0]]
# B = [[2,2],[3,3],[4,4]]
for p in B:
    x = p[0] - 1
    y = p[1] - 1
    if 0 <= x - 1 < 4:
        A[x - 1][y] = 1 - A[x - 1][y]
    if 0 <= x + 1 < 4:
        A[x + 1][y] = 1 - A[x + 1][y]
    if 0 <= y - 1 < 4:
        A[x][y - 1] = 1 - A[x][y - 1]
    if 0 <= y + 1 < 4:
        A[x][y + 1] = 1 - A[x][y + 1]
print(A)




