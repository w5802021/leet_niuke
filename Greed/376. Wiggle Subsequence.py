
def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums)

    l = 1
    state = 'begin'
    for i in range(1, len(nums)):
        if state == 'begin':
            if nums[i] > nums[i - 1]:
                state = 'up'
                l += 1
            elif nums[i] < nums[i - 1]:
                state = 'down'
                l += 1
        elif state == 'up':
            if nums[i] < nums[i - 1]:
                state = 'down'
                l += 1
        elif state == 'down':
            if nums[i] > nums[i - 1]:
                state = 'up'
                l += 1
    return l

def wiggleMaxLength1(nums):  #空间优化的DP算法
    if not nums:
        return 0

    up,down = 1,1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1
    return max(up,down)

def wiggleMaxLength2(nums):    #贪心算法
    if len(nums) < 2:
        return len(nums)
    count = 1
    diff = nums[1] - nums[0]
    if (diff > 0) | (diff < 0):
        count += 1
    prediff = diff

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]

        if (diff > 0 and prediff <= 0) | (diff < 0 and prediff >= 0):   #prediff 要包括等于号，
            count += 1
            prediff = diff
    return count

if __name__ == '__main__':
    l = [1,7,4,9,2,5]
    print(wiggleMaxLength(l))