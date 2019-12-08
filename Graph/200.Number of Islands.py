def numIslands(grid):
    '''
    题意：求岛屿的数量
    方法：DFS+遍历限定条件优化
    :param grid:
    :return:
    '''
    '''
        方法：DFS+遍历限定条件优化
        :param grid:
        :return:
        '''
    if not grid:
        return 0
    def dfs(grid, i, j):
        # 遍历过的节点清零
        grid[i][j] = '0'
        # 遍历当前结点的四个方向
        if i > 0 and grid[i - 1][j] == "1":
            dfs(grid, i - 1, j)
        if j > 0 and grid[i][j - 1] == "1":
            dfs(grid, i, j - 1)
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            dfs(grid, i + 1, j)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            dfs(grid, i, j + 1)
    # summ记录岛屿数量
    summ = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # 如果地图位置为1，dfs遍历该点的连通域，遍历完毕，得到一个岛屿计数
            if grid[i][j] == '1':
                summ += 1
                dfs(grid, i, j)
    return summ

def numIslands1( grid):
    '''
    bfs
    :param grid:
    :return:
    '''
    def bfs(grid, i, j):
        queue = [[i, j]]
        while queue:
            [i, j] = queue.pop(0)
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                bfs(grid, i, j)
                count += 1
    return count


def numIslands2(grid):
    '''
    并查集
    :param grid:
    :return:
    '''
    ########用并查集合并相关联顶点
    f = {}
    def find(x):
        f.setdefault(x, x)
        if f[x] != x:
            f[x] = find(f[x])
        return f[x]
    def union(x, y):
        f[find(x)] = find(y)
    ########
    if not grid: return 0
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                # 由于从左往右从上往下遍历，故只需要判断是否和左边、上边的格子是否有填充为'1'即可
                for x, y in [[-1, 0], [0, -1]]:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                        # grid[tmp_i][tmp_j]为左或上的点  grid[i][j]为当前点
                        union(tmp_i * col + tmp_j, i * col + j)

    res = set()
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                res.add(find((i * col + j)))
    return len(res)

#################################130########################################
def solve(board):
    '''
    题意：
    方法：DFS+限定条件
    :param board:
    :return:
    '''
    if not board: return
    row = len(board)
    col = len(board[0])
    if row < 3 or col < 3: return
    def dfs(i, j):
        # 如果i，j中有一个越界或者遇到了X则不继续扫描
        if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
            return
        # 否则把数组中的O变成#，意思是这个O和边缘是连通的
        board[i][j] = '#'
        # 之后从当前坐标开始上下左右进行递归搜索
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
    ###将边缘上的'O'都赋值为'#',同时也将矩阵中与边缘上的'O'连通的的'O'都赋值为'#'
    for i in range(row):
        dfs(i, 0)
        dfs(i, col - 1)
    for i in range(col):
        dfs(0, i)
        dfs(row - 1, i)
    # 之后再将所有的#变成O，O变成X就可以了
    for i in range(0, row):
        for j in range(0, col):
            if board[i][j] == 'O':board[i][j] = 'X'
            if board[i][j] == '#':board[i][j] = 'O'
    return board

#########################################695#####################################

def maxAreaOfIsland(grid):
    '''
    题意：求岛屿的数量
    方法：BFS+遍历限定条件优化
    :param grid:
    :return:
    '''
    if not grid:
        return 0

    def bfs(grid, i, j):
        ###遍历过的节点一定要清零
        grid[i][j] = 0
        count = 1
        ###边界不需要判断
        if i > 0 and grid[i - 1][j] == 1:
            count += bfs(grid, i - 1, j)
        if j > 0 and grid[i][j - 1] == 1:
            count += bfs(grid, i, j - 1)
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            count += bfs(grid, i + 1, j)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
            count += bfs(grid, i, j + 1)
        return count
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res = max(res,bfs(grid, i, j))
    return res


if __name__ == '__main__':
    # grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    # print(numIslands(grid))
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # print(solve(board))
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(maxAreaOfIsland(grid))