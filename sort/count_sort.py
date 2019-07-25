def countingSort(nums):

    bucket = [0] * (max(nums) + 1) # 桶的个数

    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1

    i = 0  # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums

if __name__ == '__main__':
    nums = [13,141,221,28,19,115,12]
    print(countingSort(nums))