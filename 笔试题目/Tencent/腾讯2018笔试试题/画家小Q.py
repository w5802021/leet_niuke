n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(input()))
# visited记录像素格上色次数
visited = [[0] * m for _ in range(n)]

def colorY(i,j,visited,graph):
    # 往右下搜索
    while i < n and j < m:
        if graph[i][j] == 'G' or graph[i][j] == 'Y':
            # 当像素格被'\'操作涂过后，对应visited记为1
            visited[i][j] += 1
            i += 1
            j += 1
        else:
            # 当前这一笔操作结束
            break
def colorB(i,j,visited,graph):
    # 往左下搜索
    while i < n and j >= 0:
        if graph[i][j] == 'G' or graph[i][j] == 'B':
            # 当像素格被'/'操作涂过后，对应visited记为2
            visited[i][j] += 2
            i += 1
            j -= 1
        else:
            break
def main():
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'Y' and visited[i][j] == 0:
                # colorY代表当前操作的一笔'\'
                colorY(i, j, visited, graph)
                res += 1
            if graph[i][j] == 'B' and visited[i][j] == 0:
                # colorB代表当前操作的一笔'/'
                colorB(i, j, visited, graph)
                res += 1
            # 像素格原本为Green时，需要的执行的操作
            if graph[i][j] == 'G' and visited[i][j] == 0:
                colorY(i, j, visited, graph)
                colorB(i, j, visited, graph)
                res += 2
            if graph[i][j] == 'G' and visited[i][j] == 1:
                # 之前已经用colorY操作过
                colorB(i, j, visited, graph)
                res += 1

            if graph[i][j] == 'G' and visited[i][j] == 2:
                # 之前已经用colorB操作过
                colorY(i, j, visited, graph)
                res += 1
    print(res)
if __name__ == '__main__':
    main()