import sys
import itertools


def deal(n, l):
    res = ''
    plan = []
    cost = []
    for i in range(1, n):
        res += str(i)
    for i in itertools.permutations(res, 3):
        plan.append(i)
    for i in plan:
        summ = 0
        for k,j in enumerate(i):
            if k == 0:
                summ += l[0][int(i[0])]
                summ += l[int(i[0])][int(i[1])]
            elif k == len(i)-1:
                summ += l[int(i[k])][0]
            else:
                summ += l[int(i[k])][int(i[k + 1])]
        cost.append(summ)
    return min(cost)


if __name__ == "__main__":
    # 读取第一行的n
    n = 4

    l = [[0 ,2, 6 ,5],
[2, 0, 4, 4],
[6, 4, 0, 2],
[5, 4, 2, 0]]
    print(deal(n, l))


###########################################动态规划问题