def numIslands(grid):
    '''
    题意：求岛屿的数量
    方法：BFS+遍历限定条件优化
    :param grid:
    :return:
    '''
    if not grid: return 0
    def bfs(grid, i, j):
        # 遍历过的节点一定要清零
        grid[i][j] = '0'
        # 边界不需要判断
        if i > 0 and grid[i - 1][j] == "1":
            bfs(grid, i - 1, j)
        if j > 0 and grid[i][j - 1] == "1":
            bfs(grid, i, j - 1)
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            bfs(grid, i + 1, j)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            bfs(grid, i, j + 1)

    summ = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                summ += 1
                bfs(grid, i, j)
    return summ

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
    if not grid: return 0
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