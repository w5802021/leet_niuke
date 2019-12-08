def main(nums):
    '''
    未完成AC原因：对于只有一个字符串的情况'aa'，‘acca’也是可以循环的，但是‘ac'就不能循环了
    :param nums:
    :return:
    '''
    if len(nums) == 1:
        # 更改此行
        return 'true' if nums[0][-1] == nums[0][0] else 'false'
    head = []
    end = []
    for i in nums:
        head.append(i[0])
        end.append(i[-1])
    for i in range(len(nums)):
        if head[i] == end[i-1]:
            continue
        else:
            return 'false'
    return 'true'

if __name__ == '__main__':
    nums = ['acca']
    print(main(nums))