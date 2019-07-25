import bisect

def searchRange(nums, target):
    try:
        ind = nums.index(target)
        count = nums.count(target)
        return [ind,ind+count-1]
    except:
        return [-1,-1]

def searchRange1(nums, target):
    first, last = 0, len(nums)

    while first < last:
        mid = first + (last - first) // 2
        if nums[mid] < target:
            first = mid + 1
        else:
            last = mid
    ind = first
    if ind >= len(nums):
        return [-1, -1]
    if nums[ind] != target:
        return [-1, -1]
    end = ind
    for i in range(ind + 1, len(nums)):
        if nums[i] == target:
            end += 1
        else:
            break
    return [ind,end]

def searchRange2(nums, target):
    ind = bisect.bisect_left(nums,target)                           #返回将x插入到列表a中的索引位置，如果已有x，则返回第一个x的位置
    if ind >= len(nums):
        return [-1, -1]
    if nums[ind] != target:
        return [-1, -1]
    end = bisect.bisect_right(nums, target) - 1                         #返回将x插入到列表a中的索引位置，如果已有x，则返回最后一个x位置的下一个位置
    return [ind,end]


if __name__ == '__main__':
    nums = [1]
    target = 2
    print(searchRange2(nums, target))