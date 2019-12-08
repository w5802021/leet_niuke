
# n = int(input())
# works = []
# total = 0
# for _ in range(n):
#     a,b = map(int,input().split())
#     total += b
#     works.append([a,b])

# works.sort(key = lambda x:x[1])
# cur_date = 0
# more_day = 0
#
# for i in range(n):
#     cur_date += works[i][1]
#     if cur_date > works[i][0]:
#         more_day += cur_date - works[i][0]
# print(more_day)


# dp = [float('-inf') for _ in range(total+1)]
# for i in range(0,n):
#     if j + works[i][1] > works[i][0]:
#         if dp[j + works[i][1]] == float('-inf'):
#             dp[j + works[i][1]] = j + works[i][1] - works[i][0]
#
#     for j in range(0,total+1-works[i][1]):
#             dp[j] = min(dp[j], dp[j+works[i][1]])
#         else:
#             dp[j] = min(dp[j], dp[j + works[i][1]])
#
# print(dp[total])

# def removeBoxes(nums):
#     n = len(nums)
#     dp = [[[0] * n for _ in range(n)] for _ in range(n)]
#     def helper(i, j, k):
#         if i > j:
#             return 0
#         if dp[i][j][k] != 0:
#             return dp[i][j][k]
#
#         while i < j and nums[i] == nums[i + 1]:
#             i += 1
#             k += 1
#         res = (k + 1) ** 2 + helper(i + 1, j, 0)
#         for m in range(i + 1, j + 1):
#             if nums[m] == nums[i]:
#                 res = max(res, helper(i + 1, m - 1, 0) + helper(m, j, 1 + k))
#         dp[i][j][k] = res
#         return dp[i][j][k]
#     return helper(0, n - 1, 0)
# while True:
#     nums = [int(c) for c in input().split()]
#     print(removeBoxes(nums))


# s = input()
#
# def isValid(s):
#     dic = {')': '(', ']': '[', '}': '{'}
#
#     stack = []
#     for c in s:
#         if c in dic:
#             tmp = stack.pop() if stack else '?'
#             if tmp != dic[c]:
#                 return False
#         else:
#             stack.append(c)
#     return True if not stack else False
#
# maxx = 0
# for i in range(len(s)):
#         if s[i] == '(':
#             for j in range(i,len(s)):
#                 if s[j] == ')' and isValid(s[i+1:j]):
#                     maxx = max(j - i + 1,maxx)
#
#         if s[i] == '[':
#             for j in range(i,len(s)):
#                 if s[j] == ']' and isValid(s[i+1:j]):
#                     maxx = max(j - i + 1,maxx)
# print(maxx)


nums = [int(c) for c in input().split()]

if not nums:
    print('')
    exit(0)
res = nums[0]
pre_max = nums[0]
pre_min = nums[0]
for num in nums[1:]:
    cur_max = max(pre_max * num, pre_min * num, num)
    cur_min = min(pre_max * num, pre_min * num, num)
    res = max(res, cur_max)
    pre_max = cur_max
    pre_min = cur_min
print(res)












