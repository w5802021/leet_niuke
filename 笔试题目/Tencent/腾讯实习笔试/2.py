'''
题目：
小Q所在的城镇里有一条笔直的公路，在这条公路上分布着n个村子，编号从1到n。有些村庄需要购进水果，有些村庄需要贩出水果。
设第i个村庄对水果的需求为Ai,其中Ai>0,表示该村庄需要购进水果，Ai<0表示该村需要贩出水果，假定sum(Ai)=0,即水果供求平衡。
现在把k个单位的水果从一个村庄到相邻村庄需要k块钱，请问最少需要多少运费可以满足所有村庄的需求。
'''


def myfunc(nums):
    ans, j = 0, 1
    if len(nums) == 2:
        return abs(nums[0])  # 终止条件

    if nums[0] > 0:
        flag = 1
    elif nums[0] < 0:
        flag = -1
    else:
        return myfunc(nums[1:])
    if nums[j] * flag > 0:
        j += 1
    else:  # 表示找到首个异号数字
        if abs(nums[0]) > abs(nums[j]):  # 表示异号的数的绝对值较小
            ans += abs(nums[j]) * j  # [5,-4,2,-3]--&gt;[1,0,2,-3]
            nums[0] = nums[j] + nums[0]  # 继续计算[1,0,2,-3]直到第一个数为0
            nums[j] = 0

        else:  # 若异号的数绝对值大于第一个数[3,-4,2,-1]
            ans += abs(nums[0]) * j  # [3,-4,2,-1]--&gt;[0,-1,2,-1]
            nums[j] = nums[j] + nums[0]  # [0,-1,2,-1]--&gt;[-1,2,-1]
            nums[0] = 0  # [-1,2,-1]--&gt;[0,1,-1]--&gt;[1,-1]--&gt;1
            return ans + myfunc(nums[1:])  # 同时注意费用的计算，搬移量*距离

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(myfunc(nums))



