from collections import Counter

n, k = map(int, input().split())
s = input()
# 计算得到每个数字的出现次数
d = Counter(list(map(int, s)))
res = float("inf")
ans = "A"
# i表示需要修改成的相同数字
for i in range(10):
    tmp_s = s
    # need代表还需要替换的次数
    need = k - d[i]
    cost = 0
    # gap是修改以为数字的代价  由贪心原则  选择较小的gap进行数据搜索
    gap = 1

    while need > 0:
        # i+gap为需要修改的原始数字，
        if i + gap <= 9:
            if d[i + gap] < need:
                tmp_s = tmp_s.replace(str(i + gap), str(i))
                cost += d[i + gap] * gap
                need -= d[i + gap]
            else:
                # 因为要使i+gap --> i,从左往右逐次替代能保证字典序最小
                # replace原序是从左往右
                tmp_s = tmp_s.replace(str(i + gap), str(i), need)
                cost += need * gap
                break
        # i-gap表示要变化的值小于当前值i
        if i - gap >= 0:
            if d[i - gap] < need:
                tmp_s = tmp_s.replace(str(i - gap), str(i))
                cost += d[i - gap] * gap
                need -= d[i - gap]
            else:
                # 因为要使i-gap --> i,从右往左逐次替代能保证字典序最小
                tmp_s = tmp_s[::-1]
                tmp_s = tmp_s.replace(str(i - gap), str(i), need)
                # 替换完要还原成原来的顺序
                tmp_s = tmp_s[::-1]
                cost += need * gap
                break
        gap += 1
    # 遍历10个不同的i，找出修改
    if cost < res:
        ans = tmp_s
        res = cost
    # 对于cost相同的，选择字典序最小的号码输出
    elif cost == res and tmp_s < ans:
        ans = tmp_s
print(res)
print(ans)