'''
思路：
    判断数组中是否既有偶数又有奇数，如果都有，则直接升序排列输出即为字典序最小

'''
n = 10
nums = [7,3,5,1]
# for i in range(n):
#     minn = float('inf')
#     flag = 0
#     for j in range(n):
#         if i != j and (nums[i] + nums[j]) % 2 != 0 and nums[j] < nums[i]:
#             if nums[j] < minn:
#                 minn = nums[j]
#                 min_ind = j
#                 flag = 1
#     if flag == 1:
#         nums[i],nums[min_ind] = nums[min_ind],nums[i]
# print(nums)

jishu = 0
oushu = 0
for i in nums:
    if  i % 2 == 0:
        oushu += 1
    elif i % 2 != 0:
        jishu += 1
if jishu!=0 and oushu!=0 :
    nums.sort()
    print(nums)
else:
    print(nums)





