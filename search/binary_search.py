
#
#二完全有序数组的二叉搜索
#

def binary_search(nums,target):
    first, last = 0, len(nums)
    # 没在列表中的元素能插在中间
    while first < last:
        mid = first + (last - first) // 2
        if nums[mid] < target: first = mid + 1
        else: last = mid
    return first  #若查找的数不在列表中，则返回一个可插入的索引位置，使得列表依旧按顺序排列

#
#非完全有序数组的二叉搜索   eg.[3,4,5,0,1,2]
#

def binary_search2(nums,target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
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
    nums = [65, 73, 73,90,1, 3, 4, 8, 22 ]
    tar = 23
    print(binary_search(nums,tar))