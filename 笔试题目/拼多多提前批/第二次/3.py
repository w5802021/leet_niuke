n = int(input())
nums = [int(c) for c in input().split()]
# max_bd为可能出现数字最大的骰子
max_bd = max(nums)
min_bd=1

res=0
exp_his=[]
# i为最大骰子数的所有可取数
for i in range(1,max_bd+1):
    # cur_expect记录最大数取值为i的概率
    cur_expect=1
    for num in nums:
        # exp_i 代表每个骰子的取值不超过i的概率
        exp_i=min(i/num, 1)
        # 此时cur_expect记录的是取值不超过i的概率
        cur_expect=cur_expect*exp_i
    # 去除最大数的取值为1,...,i-1的概率
    if exp_his:
        for t in exp_his:
            cur_expect=cur_expect-t
    # exp_his列表里再存下最大数取值为i的概率
    exp_his.append(cur_expect)
    res+=cur_expect*i
print('%.2f'%res)