def find_root(x,parent):
    '''
    找到当前节点的父根节点
    :param x:
    :param parent:
    :return:
    '''
    x_root = x
    while parent[x_root] != -1:
        x_root = parent[x_root]
    return x_root

def union_vertices(x,y,parent,rank):
    '''
    合并两个集合
    :param x:
    :param y:
    :param parent:
    :return:
    '''
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)
    # 合并失败，不进行合并
    if x_root == y_root:
        return 0
    # 合并x的父结点与y的父结点
    else:
        # parent[x_root] = y_root（未压缩路径，可能使长路径接到短路金父结点，增加了路径长度）
        # 压缩路径，将短路径的父结点接到长路径的父结点
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[y_root] > rank[x_root]:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[y_root] += 1
        return 1

def test():
    # 顶点数量
    num = 6
    parent = [-1] * num
    # rank记录查找路径的长度
    rank = [0] * num
    edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [2, 5]]
    for i in range(len(edges)):
        x = edges[i][0]
        y = edges[i][1]
        if union_vertices(x, y, parent,rank) == 0:
            print('检测到环')
            exit(0)
    print('未检测到环')

if __name__ == '__main__':
    test()




