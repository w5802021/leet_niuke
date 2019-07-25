
def containsDuplicate(nums):
    num = set(nums)
    if len(num) != len(nums):
        return True
    return False

######################219################
def containsDuplicate2(nums,k):
    num_dic = {}
    for i in range(len(nums)):
        if (nums[i] in num_dic) and (abs(i - num_dic[nums[i]]) <= k):
            return True
        num_dic[nums[i]] = i
    return False


if __name__ == '__main__':
    nums = [1,3,4,3,2,4,2]
    nums2 = [1,0,1,1]
    # print(containsDuplicate(nums))
    print(containsDuplicate2(nums2,0))