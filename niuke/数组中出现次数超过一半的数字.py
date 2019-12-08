
def MoreThanHalfNum_Solution(numbers):
    '''
    假设有这个数字，那么它的数量一定比其它所有数字之和还要多，按照这个思路得出num，然后验证
    '''
    if not numbers:
        return 0
    num = numbers[0]
    count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == num:
            count += 1
        else:
            count -= 1
        if count == 0:
            num = numbers[i]
            count = 1

    count = 0
    for i in numbers:
        if i == num:
            count += 1
    return num if count > len(numbers) / 2.0 else 0