'''
辗转相除法（最大公约数）
'''
def main1(a,b):
    '''
    解题步骤：
    1 通过键盘输入两个需要求解的数a，b
    2 比较两数的大小，找出较小的数，默认a为较小的数
    3 较大数b取余较小数a，如果取余结果等于较小数a，算法终止，当前a或b即为最大的公约数
    4 若取余结果不等于较小数a，则转到第二步
    '''
    def dfs(a,b):
        if a > b:
            a,b = b,a
        if b % a == 0:
            return a
        else:
            return dfs(b % a,b)

    res = dfs(a,b)
    res2 = a * b // res
    return res, res2

print(main1(10,6))

'''
更相减损法（最大公约数）
'''
def main2(a,b):
    '''
    解题步骤：
    1 通过键盘输入两个需要求解的数a，b
    2 比较两数的大小，找出较小的数，默认a为较小的数
    3 较大数b减去较小数a，如果相减结果等于较小数a，算法终止，当前a或b即为最大的公约数
    4 若减结果不等于较小数a，则转到第二步
    '''
    def dfs(a,b):
        if a > b:
            a,b = b,a
        if b - a == a:
            return a
        else:
            return dfs(b - a,a)

    res = dfs(a,b)
    res2 = a*b // res
    return res, res2

print(main2(10,6))

'''
最小公倍数       两个数的乘积 = 最大公约数 × 最小公倍数
'''

#########3个数的最大公约数与最小公倍数
def dfs(a, b):
    if a > b:
        a, b = b, a
    if b - a == a:
        return a
    else:
        return dfs(b - a, a)
def gcd_3(a,b,c):
    return dfs(dfs(a,b),c)
#利用求大公约数求最小公倍数
def maxG(a,b,c):
    return a*c*b*gcd_3(a,b,c)//(dfs(a,b)*dfs(a,c)*dfs(b,c))
print(gcd_3(5,10,6))
print(maxG(5,10,6))
