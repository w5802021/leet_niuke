def medianSlidingWindow(nums, k):
    '''
    二分法
    :param nums:
    :param k:
    :return:
    '''
    import bisect
    # window里一直是有序的数组
    window = sorted(nums[:k])
    res = []
    # 如果滑窗长度为偶数
    if k % 2 == 0:
        res.append((window[k // 2] + window[k // 2 - 1]) / 2)
    else:
        res.append(window[k // 2])

    for i in range(k, len(nums)):
        bisect.insort(window, nums[i])
        # 滑窗删除未排序前窗前的第一个数（如果用remove时间复杂度是O（n），这里用二分）
        index = bisect.bisect_left(window, nums[i - k])
        window.pop(index)
        if k % 2 == 0:
            res.append((window[k // 2] + window[k // 2 - 1]) / 2)
        else:
            res.append(window[k // 2])
    return res

from heapq import *

def medianSlidingWindow1(nums, k):
    '''
    大小堆维护
    :param nums:
    :param k:
    :return:
    '''
    # 对滑窗数组维护一个小顶堆和一个大顶堆，小顶堆存滑窗后半部分数，大顶堆存滑窗前半部分数
    # 如果k是奇数，则小顶堆中的数量比大顶堆中的数量多一个
    # 如果k是偶数，则小顶堆中的数量和大顶堆中的数量相同
    max_heap,min_heap,res = [],[],[]

    for i,n in enumerate(nums[:k]):
        heappush(max_heap, (-n,i))
    for i in range(k - k // 2):
        heappush(min_heap, (-max_heap[0][0], max_heap[0][1]))
        heappop(max_heap)

    for i,n in enumerate(nums[k:]):
        if k % 2:
            res.append(min_heap[0][0]/1.)
        else:
            res.append((min_heap[0][0] - max_heap[0][0])/2.)
        ##############
        # 如果滑窗后续数大于小顶堆的最小值，则应将其插入滑窗后半部分
        if n >= min_heap[0][0]:
            heappush(min_heap,(n,i+k))
            # nums[i]是上一次滑窗的第一个元素，判断它在小顶堆还是大顶堆中(这里如果nums[i]在大顶堆中)
            if nums[i] <= min_heap[0][0]:
                heappush(max_heap, (-min_heap[0][0], min_heap[0][1]))
                heappop(min_heap)
        else:
            heappush(max_heap,(-n,i+k))
            if nums[i] >= min_heap[0][0]:
                heappush(min_heap, (-max_heap[0][0], max_heap[0][1]))
                heappop(max_heap)
        ###
        # 删除大小堆中之前滑窗已经遍历过的数
        while(max_heap and max_heap[0][1] <= i):
            heappop(max_heap)
        while(min_heap and min_heap[0][1] <= i):
            heappop(min_heap)

    if k % 2:
        res.append(min_heap[0][0] / 1.)
    else:
        res.append((min_heap[0][0] - max_heap[0][0]) / 2.)
    return res

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(medianSlidingWindow1(nums, k))