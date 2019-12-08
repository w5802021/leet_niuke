class board:
    def __init__(self,L,W):
        self.l = L
        self.w = W
class dpc:
    def __init__(self,l,h):
        self.l = l
        self.h = h

def main(n,L,W):
    boards = []
    l = 0
    for i in range(n):
        boards.append(board(L[i],W[i]))
        l += W[i]
    # 类对象排序，先按x.w排序，再按x.l排序
    # 重量排序的优先级高于长度排序的优先级
    # 思路：先选择重量较小的木板作为塔顶，逐次往下找到合适的木板
    boards.sort(key=lambda x:(x.w,x.l))
    dp = [dpc(0,0) for _ in range(l+5)]
    summ = 0
    res = 0
    for i in range(n):
        # boards[i]代表最底部的木板
        # dp
        for j in range(summ, -1, -1):
            # j代表boards[i]上共累积的重量
            if boards[i].w * 7 >= j:
                # 寻找的boards[i]的长度应使得大于前总重量下木板的最长长度
                if dp[j].l < boards[i].l:
                    #
                    if dp[j].h+1 > dp[j+boards[i].w].h:
                        # j+boards[i].w表示选择了boards[i],当前所有木板的重量,
                        # dp[x].h表示当前总重量下最大的金字塔高度
                        # dp[x].l表示当前总重量下木板的最长长度
                        # 思路:由已经选择的木板来选择最底部的木板
                        dp[j+boards[i].w].h = dp[j].h + 1
                        dp[j+boards[i].w].l = boards[i].l
            # 找到最优高度
            res = max(res,dp[j+boards[i].w].h)
        summ += boards[i].w
    return res

def main2(n,L,W):
    boards = []
    l = 0
    for i in range(n):
        boards.append(board(L[i], W[i]))
        l += W[i]
    boards.sort(key=lambda x: (x.l, x.w))

    res = 1
    # dp[i][h]记录以第i块积木为底, 高为h的积木塔的最低重量.
    dp = [[-1] * (n+1) for _ in range(n)]
    dp[0][1] = boards[0].w

    for i in range(1,n):
        dp[i][1] = boards[i].w
        for h in range(2,n+1):
            for j in range(i-1,-1,-1):
                if dp[j][h-1] != -1 and boards[i].w * 7 >= dp[j][h-1] and (dp[i][h] == -1 or boards[i].w + dp[j][h-1] < dp[i][h]):
                    res = max(res,h)
                    dp[i][h] = boards[i].w + dp[j][h-1]

    return res


if __name__ == '__main__':
    n = 10
    L = [1,2,3,4,5,6,7,8,9,10]
    W = [1,1,1,1,1,1,1,1,1,10]
    print(main(n,L,W))