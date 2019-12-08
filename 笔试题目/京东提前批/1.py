# n = 5
#
# grid = []
# for i in range(5):
#     grid.append([int(c) for c in input().split()])
#
#
# def dfs(grid, i, j):
#     # 遍历过的节点清零
#     grid[i][j] = '0'
#     # 遍历当前结点的四个方向
#     if i > 0 and grid[i - 1][j] == "1":
#         dfs(grid, i - 1, j)
#     if j > 0 and grid[i][j - 1] == "1":
#         dfs(grid, i, j - 1)
#     if i < len(grid) - 1 and grid[i + 1][j] == "1":
#         dfs(grid, i + 1, j)
#     if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
#         dfs(grid, i, j + 1)


class sol:
    def __init__(self):
        self.visited = 0
        self.res = float('inf')

    # 计算数字相等的连通域的最大面积
    def search(self,arr,i,j,value,arrlist):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] != value:
            return 0
        arrlist.append((i,j,arr[i][j]))
        arr[i][j] = self.visited
        res = 1
        res += self.search(arr, i + 1, j, value, arrlist)
        res += self.search(arr, i - 1, j, value, arrlist)
        res += self.search(arr, i, j - 1, value, arrlist)
        res += self.search(arr, i, j + 1, value, arrlist)
        return res

    # 消去连通区的数字后进行重力下沉
    def down(self,arr):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 0:
                    continue
                else:
                    if i+1 < 5 and arr[i+1][j] == 0:
                        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

    # 消消乐时，尝试所有顺序的消去方法，找到剩余最少的方块
    def play(self,arr):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 0:
                    continue
                import copy
                arrback = copy.deepcopy(arr)
                # 存储已消去的快
                arrlist = []
                tmp = self.search(arr,i,j,arr[i][j],arrlist)
                if tmp > 3:
                    self.down(arr)
                    self.play(arr)

                arr = arrback
        tmpres = 0
        for i in range(5):
            for j in range(5):
                if arr[i][j] != 0:
                    tmpres += 1

        if tmpres < self.res:
            self.res = tmpres

    def main(self):
        n = 5
        grid = []
        for i in range(5):
            grid.append([int(c) for c in input().split()])
        self.play(grid)
        return self.res

a = sol()
print(a.main())




