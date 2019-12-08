# T = int(input())

def get_end(st,end,grid):
    e0 = end[0]
    e1 = end[1]
    # 这里题意有点问题，不知道是否需要更改起点grid的状态
    def dfs(i,j,grid):
        # 遍历到终点，且终点网格位置为'X'
        if i == e0 and j == e1 and grid[i][j] == 'X':
            return True
        # 遍历到终点，且终点网格位置为'.'
        if i == e0 and j == e1 and grid[i][j] == '.':
            if grid[i+1][j] == '0' and grid[i-1][j] == '0' and grid[i][j+1] == '0' and grid[i][j-1] == '0':
                return False
            else:
                return True
        # 遍历到非终点，且终点网格位置为'.'
        if 0 <= i < n  and 0 <= j < m and grid[i][j] == '.':
            grid[i][j] = 'X'
            if 0 <= i+1 < n  and 0 <= j < m and grid[i + 1][j] != '0':
                return dfs(i + 1, j,  grid)
            if 0 <= i-1 < n  and 0 <= j < m and grid[i - 1][j] != '0':
                return dfs(i - 1, j,  grid)
            if 0 <= i < n  and 0 <= j-1 < m and grid[i][j - 1] != '0':
                return dfs(i, j - 1,  grid)
            if 0 <= i < n  and 0 <= j+1 < m and grid[i][j + 1] != '0':
                return dfs(i, j + 1,  grid)
        # 遍历到非终点，且终点网格位置为'X'
        if 0 <= i < n and 0 <= j < m and grid[i][j] == 'X':
            grid[i][j] = '0'
            if 0 <= i+1 < n  and 0 <= j < m and grid[i + 1][j] != '0':
                return dfs(i + 1, j,  grid)
            if 0 <= i-1 < n  and 0 <= j < m and grid[i - 1][j] != '0':
                return dfs(i - 1, j,  grid)
            if 0 <= i < n  and 0 <= j-1 < m and grid[i][j - 1] != '0':
                return dfs(i, j - 1,  grid)
            if 0 <= i < n  and 0 <= j+1 < m and grid[i][j + 1] != '0':
                return dfs(i, j + 1,  grid)
        return False

    return dfs(st[0], st[1], grid)

T = 1
for _ in range(T):
    # n,m = map(int,input().split())
    # grid = []
    # for i in range(n):
    #     grid.append(list(input()))
    n,m =9,47
    # grid1 = ['X...XX','...XX.','.X..X.','......']
    grid1 = ['....X.X.X.X...X..X.....X..X..X..X....X.X...X..X',
             'XX..X...X.........X...X...X..X.XX......X...X...',
             '..XX...X.......X.....X.....X.XX..X.....X..XX...',
             '.X...XX....X...X.......X.X...X......X.X.X......',
             'X......X..X.XXX....X...X.X.XX..X.......X....X.X',
             '....XX.X...X.XXX.X..XX.XXX...XXX..XX.X.X.XX..XX',
             '.........X...X.XXXX...XX.XX....XX..X...X....X..',
             '.............X....XXXX....X.X...XX.XX.X.X..X...',
             '.X......X.....X......X......X.X.X..X.......XXX.']
    grid = [list(x) for x in grid1]

    # st = list(input().split())
    # end = list(input().split())
    st = [1,33]
    end=[6,29]

    if get_end(st,end,grid):
        print('YES')
    else:
        print('NO')

