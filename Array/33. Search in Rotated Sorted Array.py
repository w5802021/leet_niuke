
def search(nums, target):
    try:
        ind = nums.index(target)    #内置函数
    except:
        ind = -1
    return ind

def search1(nums, target):

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) >> 1
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:  # 二分后前半段是升序
            if nums[low] <= target <= nums[mid]:  # 目标在前半段
                high = mid - 1
            else:
                low = mid + 1
        else:  # 二分后前半段不是升序
            if nums[mid] <= target <= nums[high]:  # 目标在后半段
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search1(nums, target))