class permutation:
    '''
    题型：带限定条件的排列问题
    '''
    def __init__(self,arr):
        self.nums = arr
        self.n = len(self.nums)
        self.visited = [None]*self.n
        self.graph = [[None]*self.n for _ in range(self.n)]
        self.comb = ''
        # 这里采用集合来存储答案是因为重复的数会多计算一次相同的组合，采用hash集合进行过滤
        self.res = set()

    def dfs(self,start):
        self.visited[start] = True
        self.comb += str(self.nums[start])
        if len(self.comb) == self.n:
            # 将字符串第3位不为'4'的组合存下
            if self.comb.index('4') != 2:
                self.res.add(self.comb)

        for j in range(self.n):
            if self.graph[start][j] == 1 and self.visited[j] == False:
                self.dfs(j)

        self.comb = self.comb[:-1]
        self.visited[start] = False

    def getallcomb(self):
        # 构建图的关系
        for i in range(self.n):
            for j in range(self.n):
                if i==j:
                    self.graph[i][j] = 0
                else:
                    self.graph[i][j] = 1
        # 组合中3与5不能直接连接
        self.graph[3][5] = 0
        self.graph[5][3] = 0
        # 以每个节点作为开始节点进行深度遍历
        for i in range(self.n):
            self.dfs(i)

        return self.res

if __name__ == '__main__':
    arr = [1,2,2,3,4,5]
    t = permutation(arr)
    print(t.getallcomb())
