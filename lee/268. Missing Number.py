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

#######################260###################只出现一次的数字III
def FindNumsAppearOnce(array):
    '''
    思路：
    1 在基础题目中，数组中所有数字异或得到单独数字；那么在这个题目中，数组中所有数字异或得到这两个单独数字的异或，比如是x；

    2 我们只需要把数组中所有数字分成两组，并且每一组中的仅包含一个单独数字，那么就把这个问题转化为基础问题了，比如:数组:[a,b,c,d,a,b]
    转换为[a,a,c],[b,b,d]，或者是[a,a,d],[b,b,c],这没区别，就把这个问题转换成了基础问题了，问题在于如何转换

    3 x是两个不相同数字的异或，那么x必然不是0，我们只要找到x为1的某一位，比如第n位，或者m位，只要是x在这一位上为1。那么在这一位上，
      c,d是不同的，异或运算才得到1，否则就是0了。，这就是区分c,d的关键

    4 遍历数组，当第n位为1的时，归位一组，第n位不为1，归为另一组。这样就得到了两个组，将问题成功转换为夹出问题

    '''
    # 得到的accumulate是两个单独数字的异或
    accumulate = 0
    nums = array
    for n in nums:
        accumulate ^= n

    # 左移mask，移动到xor为1的那一位，也是单独数字存在差异的一位  mask都是10000...的形式
    mask = 1
    while (mask & accumulate) == 0:
        mask <<= 1

    #num1,num2代表数组将数组划分为两部分的 累积异或
    acc1, acc2 = 0, 0
    for n in nums:
        # 按照差异，对数组分组，两个单独数字被分到不同的组    这样划分后，每个不同分组的元素是不平等
        if n & mask == 0:
            acc1 ^= n
        else:
            acc2 ^= n

    return [acc1, acc2]

if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    # print(missingNumber2(nums))
    nums2 = [4,1,2,1,2]
    # print(singleNumber(nums2))
    nums3 = [0,1,0,1,0,1,99]
    aaa = [1,2,1,2,3,4]
    print(FindNumsAppearOnce(aaa))