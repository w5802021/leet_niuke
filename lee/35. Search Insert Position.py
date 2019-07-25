
def searchInsert(nums,target):   #二分查找解决    注意 这种不能解决列表中有重复数的情况  但是能解决没在列表中的元素能插在其后面索引后面
    fir, last = 0, len(nums)

    while (last - fir >= 1):   #注意这个条件

        mid = (fir + last) // 2

        if nums[mid] < target:
            fir = mid + 1
        elif nums[mid] > target:
            last = mid
        else:
            return (mid)
    return (fir)


if __name__ ==  '__main__':
    nums =  [1,2,3,4,5]
    val = 6
    print(searchInsert(nums,val))