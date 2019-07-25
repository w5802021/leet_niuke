def findMin( nums) :
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[low] < nums[mid]:
            low = mid + 1

        if nums[high] > nums[mid]:
            high = mid - 1


if __name__ == '__main__':
    nums =[3,4,5,1,2]
    print(findMin(nums))