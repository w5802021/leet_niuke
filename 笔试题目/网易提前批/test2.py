'''
思路：
    排序后除了最大的那个数，其余的数必然满足那个条件啊，因为只是前面的那个数就比它大了，
    所以只要给最大的那个数找两侧的数就可以了，两侧最大的数就是第二大第三大的数，如果这两数都不满足条件，
    那么必然无法排成，如果满足 那必然能排成圆环
'''
t = 1
for i in range(t):
    n = 5
    nums = [1,2,2,2,4]

    nums.sort()
    nums[n-1],nums[n-2] = nums[n-2],nums[n-1]
    flag = 0

    if nums[n-2] >= nums[n-1] + nums[n-3]:
        flag = 1
    if flag:
        print('NO')
    else:
        print('YES')

