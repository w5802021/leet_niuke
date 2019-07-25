def subsets(nums):                #递归法
    def dfs(nums, mask, c, res):              # c用来判断mask是否遍历完毕
        if len(nums) == c:
            tmp = [nums[i] for i in range(len(mask)) if mask[i] == 1]  #将遍历完毕的mask数组中 ，将标有1下标 对应其nums中的元素，存入结果
            res.append(tmp)

        else:                             #整体思想：mask中每一位为0或1的状态下，由递归展开出所有其他位的情况
            mask[c] = 1
            dfs(nums, mask, c+1, res)
            mask[c] = 0
            dfs(nums, mask, c+1, res)

    res = []
    mask = [0 for _ in range(len(nums))]
    dfs(nums, mask, 0, res)
    return res

def subsets1(nums):  #迭代法
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
def subsetsWithDup(nums):                      #若列表集合存在重复元素
    nums.sort()
    res=[[]]
    for i in range(len(nums)):
        if(i==0 or nums[i]!=nums[i-1]):         #当为首元素或该元素在列表没有有相同元素时
            l=len(res)
            for t in range(len(res)):
                res.append(res[t]+[nums[i]])
        else:
            p=len(res)
            for t in range(l,len(res)):          #因为有相同元素的存在，相同元素已经遍历过的无需在遍历
                res.append(res[t]+[nums[i]])
            l=p
    return res

if __name__ == '__main__':
    # nums = [1,2,3]
    # print(subsets1(nums))
    nums = [1, 2, 2]
    print(subsetsWithDup(nums))

