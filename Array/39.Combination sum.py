############################################################################
def combinationSum1(candidates,target):
    '''
    解题要点：1、candidates数组不含有重复元素
             2、res中tmp每一项中可以包含重复元素
             3、解集不能包含重复的组合
    '''
    candidates.sort()
    n = len(candidates)
    res = []
    def backtrack(remain,first,tmp):
        # first为回溯列表中第一个数的索引
        if remain < 0 or first == n:
            return
        if remain == 0:
            res.append(tmp)
            return
        for i in range(first,n):
            # 加入该约束条件大大提高程序运行速度
            if candidates[i] > remain:
                break
            backtrack(remain - candidates[i],i,tmp + [candidates[i]])
    backtrack(target,0,[])
    return res

####################################40###########################################

def combinationSum2(candidates,target):
    '''
    解题要点：1、candidates数组含有重复元素
             2、candidates中的每个数字在每个组合中只能使用一次
             3、解集不能包含重复的组合
    '''
    res = []
    candidates.sort()

    def backtrack(candidates, remain, tmp):
        if remain == 0:
            res.append(tmp)
            return
        if not candidates or candidates[0] > remain:
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remain:
                return
            backtrack(candidates[i + 1:], remain - candidates[i], tmp + [candidates[i]])

    backtrack(candidates, target, [])
    return res

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    candidates2 = [10,1,2,7,6,1,5]
    target2 = 8
    # print(combinationSum1(candidates,target))
    print(combinationSum2(candidates2,target2))
