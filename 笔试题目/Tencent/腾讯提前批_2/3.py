'''
总结：关键是对数论中的逆元取模（即分数的取模方式）不熟悉
'''

n,p,q = map(int,input().split())
mod = 10**9 + 7

# 逆元模板
def inv(x):
    global mod
    if(x==1):
        return 1
    return (mod-mod//x)*inv(mod%x)%mod
# 求两个数的最大公约数
def fun(a,b):
    x = a % b
    while (x != 0):
        a = b
        b = x
        x = a % b
    return b
# n_chan代表所有符合条件的组合数
n_chan = 0
num = 0
i = p
while i <= n-q:
    summ = 1
    if i == p:
        # 求出C(N,P)
        summ = 1
        for j in range(i, 0, -1):
            summ *= (n - (i - j)) / j
        cn = summ
        # 求期望的分子部分
        num += i * cn
    else:
        # 递推依次求 C(n,p+1),...,C(n,n-q)
        cn = cn*(n-(i-1))/i
        num += i * cn
    #C(n,p)+C(n,p+1)+...+C(n,n-q)
    n_chan += cn
    i += 1

den = n_chan
gongyue = fun(num,den)
# 约分分子分母
num = num//gongyue
den = den//gongyue
print(int(num//gongyue*inv(den))%mod)



