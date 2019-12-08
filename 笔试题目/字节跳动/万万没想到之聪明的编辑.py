

# 1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
# 2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
# 3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC


n = int(input())
for _ in range(n):
    s = input()
    # res存储不被删除的数
    res = []

    for e in s:
        if len(res) < 2:
            res.append(e)
            continue
        # 判断AAA型
        if len(res) >= 2:
            if e == res[-1] and e == res[-2]:
                continue
        # 判断AABB型
        if len(res) >= 3:
            if e == res[-1] and res[-2] == res[-3]:
                continue
        res.append(e)
    print("".join(res))

