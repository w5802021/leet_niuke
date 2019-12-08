s = input()
nums = [int(x) for x in s.split()]
# nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 7, 7, 9]
dic = {1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4}

def isHu(nums):
    """
    判断是否可以胡牌
    思路：从最小的数字开始尝试，如果把其当成雀头成员，该数字划掉两个，并看余下的数字能否划空
                             如果是刻子成员，该数字划掉三个，并查看余下数字能否划空
                             如果是顺子成员，划掉该值 a ,a+1,a+2，并查看余下数字能否划空
            如果上述三种尝试都无法划空数组，说明存在数字无法是 雀头、刻子、顺子的成员， 即无法胡牌。
            （上述任何一种情况能划空数组，都可以胡牌）
    :param nums:
    :return:
    """
    if not nums:
        return True
    n = len(nums)
    count0 = nums.count(nums[0])
    # 这里为什么用n%3来检验的原因是，并不是每次雀头都是最开始尝试的首尾数字，如果雀头出现在数组后面，则需根据数组长度来判断是否有确定雀头
    if n % 3 != 0 and count0 >= 2 and isHu(nums[2:]) == True:
        return True

    if count0 >= 3 and isHu(nums[3:]) == True:
        return True

    if nums[0] + 1 in nums and nums[0] + 2 in nums:
        last_nums = nums.copy()
        last_nums.remove(nums[0])
        last_nums.remove(nums[0] + 1)
        last_nums.remove(nums[0] + 2)
        if isHu(last_nums) == True:
            return True
    # 以上条件都不满足，则不能和牌
    return False

def main(nums):
    res = []
    for i in nums:
        dic[i] -= 1
    # 遍历尝试加入每种数字，判断是否能和牌
    for last in range(1,10):
        if dic[last] > 0:
            total_pai = nums+[last]
        else:
            continue
        total_pai.sort()
        if isHu(total_pai):
            res.append(last)
    res.sort()
    return ' '.join(str(c) for c in res) if res else '0'

if __name__ == '__main__':
    print(main(nums))
