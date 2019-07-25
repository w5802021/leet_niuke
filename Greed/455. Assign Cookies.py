def findContentChildren(g, s):    #####遍历不同的列表产生的算法复杂度和处理方法不同
    count = 0
    g.sort(reverse=False)
    s.sort(reverse=False)

    for gi in g:
        for i, si in enumerate(s):
            if gi <= si:
                del s[i]
                count += 1
                break
    return count

def findContentChildren1(g, s):
    count = 0
    g.sort(reverse=False)
    s.sort(reverse=False)

    for si in s:
        if g[count] <= si:
            count += 1
            if count == len(g):
                break
    return count

if __name__ == '__main__':
    g =[1,2]
    s =[1,2,3]
    print(findContentChildren(g,s))