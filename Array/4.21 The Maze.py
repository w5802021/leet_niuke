def getpath(maze,x,y,slo):
    N = len(maze)
    if x == N-1 and y == N-1:
        slo[x][y] = 1
        return True

    if x>=0 and x<N and y>=0 and y < N and maze[x][y] == 1:
        slo[x][y] = 1

        if getpath(maze,x+1,y,slo):
            return True
        if getpath(maze,x,y+1,slo):
            return True

        slo[x][y] = 0
        return False
    return False

if __name__ == '__main__':
    maze = [[1,0,0,0],
            [1,1,0,1],
            [0,1,0,0],
            [1,1,1,1]]

    slo = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

    if getpath(maze,0,0,slo):
        print(slo)