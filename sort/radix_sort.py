
def radix_sort(nums):
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))  # 最大数的位数决定了外循环多少次
    buckets = [[] for _ in range(mod)]  # 构造 mod 个空桶

    while mostBit:
        for num in nums:  # 将数据放入对应的桶中
            buckets[num // div % mod].append(num)

        i = 0
        for bucket in buckets:           # 将数据收集起来
            while bucket:
                nums[i] = bucket.pop(0)  # 依次取出
                i += 1

        div *= 10  #进位，由地位到高位桶排序
        mostBit -= 1
        
    return nums

if __name__ == '__main__':
    nums = [13,141,221,28,19,115,12]
    print(radix_sort(nums))