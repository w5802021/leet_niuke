def dominantIndex(nums):
    num = nums.copy()
    nums.sort()

    if len(nums) < 1:
        return -1

    if len(nums) == 1:
        return 0

    if nums[-1] >= 2 * nums[-2]:
        return num.index(nums[-1])
    else:
        return -1

if __name__ == '__main__':
    nums = [0,0,0,1]
    print(dominantIndex(nums))