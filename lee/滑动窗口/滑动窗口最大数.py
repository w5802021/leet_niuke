def maxInWindows(nums, k):

    if k == 0:
        return []
    if k > len(nums):
        return []
    import bisect
    # window里一直是有序的数组
    window = sorted(nums[:k])
    res = []
    res.append(window[-1])

    for i in range(k, len(nums)):
        bisect.insort(window, nums[i])
        # 滑窗删除未排序前窗前的第一个数（如果用remove时间复杂度是O（n），这里用二分）
        index = bisect.bisect_left(window, nums[i - k])
        window.pop(index)
        res.append(window[-1])
    return res

if __name__ == '__main__':

    num = [2,3,4,2,6,2,5,1]
    size = 3
    print(maxInWindows(num, size))