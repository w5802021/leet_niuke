
def rotate(nums,k):    ###insert方法耗时  时间复杂度O（n^2）
    for i in range(k):

        nums.insert(0,nums[-1-i])
    del nums[-k:]
    return nums

def rotate2(nums,k):    #####
    k = k % len(nums)   #如果k大于数组长度
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    # print(rotate(nums, k))
    print(rotate2(nums, k))