def subsets(nums):
    '''
    题意：
    不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    解集不能包含重复的子集。
    回溯法
    :param nums:
    :return:
    '''
    def backtrack(first, tmp):
        res.append(tmp)
        for i in range(first, len(nums)):
            backtrack(i + 1, tmp + [nums[i]])
    res = []
    backtrack(0,[])
    return res

def subsets1(nums):
    import itertools
    res = []
    for i in range(len(nums)+1):
        # itertools.combinations(nums, i)表示以nums中的i个元素进行组合
        for tmp in itertools.combinations(nums, i):
            res.append(tmp)
    return res

def subsets2(nums):
    # 迭代法
    if not nums:
        return [[]]
    res = [[nums[0]]]
    for i in range(1, len(nums)):
        lens = len(res)
        for j in range(lens):
            res.append(res[j] + [nums[i]])
        res.append([nums[i]])
    res.append([])
    return res

#####################################  90 ###########################################
def subsetsWithDup(nums):
    '''
    回溯法
    :param nums:
    :return:
    '''
    def backtrack(first, tmp):
        res.append(tmp)
        for i in range(first, len(nums)):
            # 剪枝
            if i > first and nums[i] == nums[i - 1]:
                continue
            backtrack(i + 1, tmp + [nums[i]])
    res = []
    nums.sort()
    backtrack(0, [])
    return res

def subsetsWithDup1(nums):                      #若列表集合存在重复元素
    '''
    题意：可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
         解集不能包含重复的子集。
    :param nums:
    :return:
    '''
    nums.sort()
    res = [[]]
    cur = []
    for i in range(len(nums)):
        # 当为首元素或该元素在列表没有有相同元素时
        if(i==0 or nums[i]!=nums[i-1]):
            cur = [tmp + [nums[i]] for tmp in res]
        else:
           #因为有相同元素的存在，相同元素已经遍历过的无需在遍历
           cur = [tmp + [nums[i]] for tmp in cur]
        res += cur
    return res

if __name__ == '__main__':
    # nums = [1,2,3]
    # print(subsets1(nums))
    nums = [1, 2, 2]
    print(subsetsWithDup(nums))

