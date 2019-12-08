#############################相似题目46####################  全排列
def permutation(string):
    def backtrack(first):
        if first == n:
            res.append(string[:])
            return
        for i in range(first,n):
            # 字符串是一种不可变的数据类型，不能直接用数组索引修改其值
            string[first], string[i] = string[i], string[first]
            backtrack(first+1)
            # 递归交换了相邻顺序的字符，结束后要将其交换回原位置
            string[first], string[i] = string[i], string[first]

    res = []
    n = len(string)
    backtrack(0)
    return res

###########################47#############################  全排列2   排列数组存在相同的值
def permuteUnique(nums):
    def backtrack(nums, first):
        if first == n:
            # 为防止递归时交换数组顺序导致的错误，递归函数的数组都要用拷贝进行传递
            res.append(nums.copy())
            return
        for i in range(first, n):
            # 剪枝(注意组合与排列剪枝条件的区别)
            if i > first and nums[first] == nums[i]:
                continue
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(nums.copy(), first + 1)
            # 这里由于使用数组的拷贝，因此不需要在递归结束后再将交换的字符交换回来
    # 先对排列数组进行排序
    nums.sort()
    res = []
    n = len(nums)
    backtrack(nums, 0)
    return res

if __name__ == '__main__':
    # s = 'abc'
    # s = list(s)
    # print([''.join(x) for x in permutation(s)])
    nums = "abc"
    nums = list(nums)
    print([''.join(x) for x in permutation(nums)])

