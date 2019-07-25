def shellsort(nums):
    ll = len(nums)
    gap = 1
    while gap < ll//3:     # 动态定义间隔序列
        gap = gap *3 + 1

    while gap > 0:
        for i in range(gap,ll):
            cur,preind = nums[i],i-gap                  # cur保存当前待插入的数
            while preind >= 0 and cur < nums[preind]:   # 插入排序
                nums[preind + gap] = nums[preind]       # 将比 cur 大的元素向后移动
                preind -= gap
            nums[preind + gap] = cur

        gap //= 3        #移动到下一个动态间隔
    return nums

if __name__ == '__main__':
    nums = [13, 141, 221, 28, 19, 115, 12]
    print(shellsort(nums))