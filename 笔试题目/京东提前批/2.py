'''
构造一个迷宫是很麻烦的一件事情，因此有人提出了一种迷宫生成方法，与铺砖的方法类似，
首先设计一个n*m的单位迷宫，然后就像铺砖一样，将这个单位迷宫复制拼接起来，如果能够通
过这种方式生成的迷宫可以
从起始位置通向无穷多的位置，那么我们认为这个单位迷宫是合法的
（每个单位不可旋转）。单位迷宫的表示包含三种符号,‘#’,‘.’和‘S’，其中‘#’代表墙，‘.’代表没
有障碍物可以通过的，S则代表的是起始位置，当然迷宫是只有一个起点的，你可以任选一个单位迷宫的
S位置作为起点，其他单位迷宫的S则视为可通行的。
'''

# 思路：将每个base版块复制9份组成一个大的grid，从中间的版块往外面递归遍历，若能找到一条路径到达grid的边界，则合适
T = int(input())

def can_get_border(si, sj, grid):
    def dfs(si, sj, grid):
        if si < 0 or si >= len(grid) or sj < 0 or sj >= len(grid[0]) :
            return
        if grid[si][sj] != '0' and grid[si][sj] != '#':
            grid[si][sj] = '0'
            dfs(si+1, sj, grid)
            dfs(si-1, sj, grid)
            dfs(si, sj+1, grid)
            dfs(si, sj-1, grid)
    dfs(si, sj, grid)
    for i in range(len(grid)):
        if grid[i][0] == '0' or grid[i][len(grid[0]) - 1] == '0':
            return True
    for j in range(len(grid[0])):
        if grid[0][j] == '0' or grid[len(grid) - 1][j] == '0':
            return True


for _ in range(T):
    n,m = map(int,input().split())
    #复制9分
    grid = []
    for i in range(n):
        a = list(input())
        grid.append(a+a+a)
    ss = grid
    for i in range(n):
        grid.append(grid[i].copy())
    for i in range(n):
        grid.append(grid[i].copy())
    for i in range(n):
        for j in range(m):
            if ss[i][j] == 'S':
                si = i
                sj = j
    if can_get_border(si+n,sj+m,grid):
        print('Yes')
    else:
        print('NO')

# 2
# 2 2
# S#
# #.
# 3 3
# ...
# ###
# #S#