#思路
# 对于N个数中任意两个数a,b(a!=b)考虑先后顺序 ， 有(a,b)及(b,a)两种情况
# 对于其中的(a,b)情况有，将其视为一个整体，插入到剩下的(N-2)个数中，有(N-1)种方法，同时剩下的N-2个数有(N-2)!种组合方式
#                   进而推出对N!个序列有(N-1)!种情况。
# 同理对(b,a)也有(N-1)!种情况。
# 一共有C(N,2)对数对，对于(a,b)及(b,a)移动代价相同，所以只需求出C(N,2)对数的代价P
# 最后  P * 2 * ((N-1)!) 即为最终解

# N = int(input())
# X = [int(c) for c in input().split()]
N = 5
X = [0,1,3,5,8]
mod = 10**9+7


def jie(num):
    '''
    计算(num)!
    :param num:
    :return:
    '''
    plus = 1
    while num:
        plus = (plus*num)%mod
        num -= 1
    return plus

summ = 0
tmp = 0

''' 
for i in range(N): 
    for j in range(i+1,N):
        tmp=(X[j]-X[i])
        sum=(sum+tmp)%mod
'''
 # 在上面基础优化
for i in range(1,len(X)):
    # tmp为当前
    tmp = (tmp + X[i-1])%mod
    # summ:上一轮的代价  X[i]*i-tmp为加入X[i]后，新增的权重代价
    summ = (summ + (X[i]*i-tmp))%mod

# 2 * (N-1)!
count = jie(N-1)*2 % mod
print((summ*count) % mod)