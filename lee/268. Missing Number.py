######################这种类型的题都有三种解法可以解决
######1.sum
######2.异或等逻辑运算
######3.哈希表存储

def missingNumber(nums):
    ml = len(nums)
    return int(ml * (ml + 1) / 2 - sum(nums))

def missingNumber2(nums):     #采用异或操作， 可防止sum的数很大越界
    summ = len(nums)
    for i in range(len(nums)):
        summ ^= nums[i]     #summ的总数  =  nums的总数 + 1
        summ ^= i
    return summ

###############136###############
def singleNumber( nums):         #一个二进制位只能表示0或者1。也就是天生可以记录一个数出现了一次还是两次
    summ = 0
    for i in nums:
        summ ^= i
    return summ

def singleNumber12( nums):
    return 2*sum(set(nums)) - sum(nums)

###############137#################
def singleNumber21(nums):         #记录出现3次，需要两个二进制位。那么上面单独的x就不行了。我们需要两个变量，每个变量取一位：
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    return list (dic.keys()) [list (dic.values()).index (1)]

def singleNumber22(nums):         #记录出现3次，需要两个二进制位。那么上面单独的x就不行了。我们需要两个变量，每个变量取一位：
    a,b = 0,0
    for i in nums:
        b = (b ^ i) & ~a
        a = (a ^ i) & ~b
    return b

def singleNumber23(nums):
    return (3*sum(set(nums)) - sum(nums))//2

if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    # print(missingNumber2(nums))
    nums2 = [4,1,2,1,2]
    # print(singleNumber(nums2))
    nums3 = [0,1,0,1,0,1,99]
    print(singleNumber23(nums3))