def deal(n, m, lmachine, ltask):
    # 完成的任务数要最大 获得的收益也要最大
    lmachine.sort(key=lambda x: (x.time, x.level), reverse=True)
    ltask.sort(key=lambda x: (x.time, x.level), reverse=True)
    # 最大能完成的任务数量及收益
    profit = 0
    count = 0

    level = [0] * 105
    j = 0
    # 对于任务i，找到一个最合适的机器去完成它
    for i in range(m):
        # 机器j若满足任务i时间要求，level数组存储已遍历机器的机器等级
        while j < n and lmachine[j].time >= ltask[i].time:
            level[lmachine[j].level] += 1
            j += 1
        # 遍历找得最小的k来完成任务的机器等级
        for k in range(ltask[i].level, 101):
            if level[k]:
                count += 1
                level[k] -= 1
                profit += 200 * ltask[i].time + 3 * ltask[i].level
                break
    return count, profit

class node:
    def __init__(self, time, level):
        self.time = time
        self.level = level

if __name__ == '__main__':
    n, m = map(int,input().split())
    lmachine = []
    ltask = []
    for i in range(n):
        b = input().split()
        machine = node(int(b[0]), int(b[1]))
        lmachine.append(machine)
    for j in range(m):
        c = input().split()
        task = node(int(c[0]), int(c[1]))
        ltask.append(task)

    count, profit = deal(n, m, lmachine, ltask)
    print(count, profit)
