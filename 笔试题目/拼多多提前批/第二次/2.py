class sol:
    def __init__(self):
        self.res = []

    def helper(self, s1, s2, t, T, index):
        '''
        :param s1:
        :param s2:
        :param t:表示新序列的字符串
        :param T:将s1转化为t所需要执行的操作
        :param index:操作s1的总次数
        :return:
        '''
        # 停止条件
        if index == len(s1):
            if (s2 == t) and T not in self.res:
                self.res.append(T)
            return
        self.helper(s1, s2, t, T + "d", index + 1)
        self.helper(s1, s2, s1[index] + t, T + "l", index + 1)
        self.helper(s1, s2, t + s1[index], T + "r", index + 1)

    def main(self):
        # 局数
        n = int(input())
        # 每一局的
        while n > 0:
            s1 = input()
            s2 = input()
            # 每一局都需要重新清理结果列表
            self.res = []
            self.helper(s1, s2, "", "", 0)
            # 输出
            print("{")
            for k in self.res:
                print(' '.join(c for c in k))
            print("}")
            n -= 1
test = sol()
test.main()

