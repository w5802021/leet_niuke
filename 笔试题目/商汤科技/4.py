
n,m = map(int,input().split())
# n,m = 5, 2
mod = 10**9 + 7

tmp = 657049
nums = []
for _ in range(n):
    if _ == 0:
        nums.append(tmp)
    else:
        tmp = (tmp**2) % mod
        nums.append(tmp)

def medianSlidingWindow(nums, k):

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

if __name__ == '__main__':
    k = m
    res = medianSlidingWindow(nums, k)
    target = sum(res)
    if target == int(target):
        res = int(target)
        print(res)
    else:
        res = (int(target)+ 0.5)
        print('%.1f' %res)


