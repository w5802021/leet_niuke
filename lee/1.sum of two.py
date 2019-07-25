def twoSum(nums, target):

    dic = {}
    for n,i in enumerate(nums):
        if i in dic:
            return [dic[i], n]
        dic[target - i] = n

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums,target))