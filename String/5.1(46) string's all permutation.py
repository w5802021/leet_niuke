#############################相似题目46####################  全排列
def permutation(string):
    res = []
    n = len(string)
    def backtrack(first = 0):
        if first == n:
            res.append(string[:])
            return
        for i in range(first,n):
            # 字符串是一种不可变的数据类型，不能直接用数组索引修改其值
            string[first],string[i] = string[i],string[first]
            backtrack(first+1)
            string[first], string[i] = string[i], string[first]
    backtrack()
    return res

###########################47#############################  全排列2   排列数组存在相同的值
def permuteUnique(nums):
    def backtrack(nums, left, right):
        if left == right:
            # 为防止递归时交换数组顺序导致的错误，递归函数的数组都要用拷贝进行传递
            res.append(nums.copy())
            return
        for i in range(left, right + 1):
            # 数组中相邻的相同元素
            if i != left and nums[left] == nums[i]:
                continue
            nums[left], nums[i] = nums[i], nums[left]
            backtrack(nums.copy(), left + 1, right)
    # 先对排列数组进行排序
    nums.sort()
    res = []
    backtrack(nums, 0, len(nums) - 1)
    return res

if __name__ == '__main__':
    # s = 'abc'
    # s = list(s)
    # print([''.join(x) for x in permutation(s)])

    nums = '122345'
    nums = list(nums)
    print([''.join(x) for x in permuteUnique(nums)])
