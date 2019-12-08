#####遍历不同的列表产生的算法复杂度和处理方法不同
def findContentChildren(g, s):
    count = 0
    g.sort()
    s.sort()

    for gi in g:
        for i, si in enumerate(s):
            if gi <= si:
                del s[i]
                count += 1
                break
    return count

def findContentChildren1(g, s):
    count = 0
    g.sort()
    s.sort()
    # 田忌赛马原则，用尺寸尽量少的饼干来先满足胃口小的孩子
    for si in s:

        if g[count] <= si:
            count += 1
            if count == len(g):
                break
        # 如果当前饼干尺寸不能满足当前小孩的胃口，则换用大一点的饼干尺寸来满足当前小孩
    return count

if __name__ == '__main__':
    g =[1,2]
    s =[1,2,3]
    print(findContentChildren(g,s))