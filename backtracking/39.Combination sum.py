def combinationSum1(candidates,target):
    '''
    回溯法
    解题要点：1、candidates数组不含有重复元素
             2、res中tmp每一项中可以包含重复元素
             3、解集不能包含重复的组合
    '''
    def backtrack(first, remain, tmp):
        # 停止条件
        if remain == 0:
            res.append(tmp)
            return
        if remain < candidates[first]:
            return
        # 回溯递归
        for i in range(first, len(candidates)):
            # 剪枝
            if candidates[i] > remain:
                break
            # 后续可能还需要用到candidates[i]
            backtrack(i, remain - candidates[i], tmp + [candidates[i]])
    res = []
    candidates.sort()
    backtrack(0, target, [])
    return res

####################################40###########################################
def combinationSum2(candidates,target):
    '''
    解题要点：1、candidates数组含有重复元素
             2、candidates中的每个数字在每个组合中只能使用一次
             3、解集不能包含重复的组合
    '''
    def backtrack(first, remain, tmp):
        # 停止条件
        if remain == 0:
            res.append(tmp)
            return
        if not candidates or remain < 0:
            return
        # 回溯递归
        for i in range(first,len(candidates)):
            # （剪枝）遇到相同的数跳过
            if i > first and candidates[i] == candidates[i - 1]:
                continue
            # 同上
            if candidates[i] > remain:
                break
            # candidates[i]已经取过，后续不能再使用
            backtrack(i + 1, remain - candidates[i], tmp + [candidates[i]])
    res = []
    candidates.sort()
    backtrack(0, target, [])
    return res

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    candidates2 = [10,1,2,7,6,1,5]
    target2 = 8
    # print(combinationSum1(candidates,target))
    print(combinationSum2(candidates2,target2))
