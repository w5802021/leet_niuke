

def bfs(grid, begin, end):
    '''
    bfs方法能求得最短路径
    :param grid:
    :param begin:
    :param end:
    :return:
    '''
    n= len(grid)
    seen = []
    dx = [1, 0, -1, 0]  # 四个方位
    dy = [0, 1, 0, -1]
    level = []
    level.append(begin)
    seen.append(begin)
    step = 0
    while level:
        queue = []
        step += 1
        for q in level:
            for i in range(4):
                nx, ny = q[0] + dx[i], q[1] + dy[i]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#':
                    if [nx, ny ] in end:
                        return step
                    if [nx, ny] not in queue and [nx, ny] not in seen:
                        queue.append([nx, ny])
                        seen.append([nx, ny])
        level = queue
        print(level)
    return -1

if __name__ == '__main__':
    n = int(input())
    grid = [['' for _ in range(n)] for _ in range(n)]
    g3 = []
    begin = []
    end = []
    # 复制9块迷宫  从中间那块迷宫的起点'S'出发，直到到达任意9块迷宫中的'E'
    for i in range(n):
        s = input()
        g3.append(s*3)
        grid[i] = list(s)
        if 'S' in s:
            begin.append(i+n)
            begin.append(s.index('S')+n)
        if 'E' in s:
            for x in range(0,2*n+1,n):
                for y in range(0,2*n+1,n):
                    end.append([i + x,s.index('E') + y])
    maze = []
    for i in range(3):
        for j in range(len(g3)):
            maze.append(g3[j])
    print(bfs(maze, begin, end))


