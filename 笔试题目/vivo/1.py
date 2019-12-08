# s = '(((0)))'
#
# count1 = 0
#
# for i in s:
#     if i == '(':
#         count1 += 1
#     if i == '0':
#         break
#
# count2 = 0
# for j in range(len(s)-1,-1,-1):
#     if s[j] == ')':
#         count2 += 1
#     if s[j] == '0':
#         break
# res = min(count1,count2)
# print(res)

# app_list = [[5,1,1000],[2,3,3000],[5,2,15000],[10,4,16000]]
# disk = 15
# mem = 10
# n = len(app_list)
#
# dp = [[0 for _ in range(mem+1)] for _ in range(disk+1)]
# for i in range(0,n):
#     for j in range(disk,app_list[i][0]-1,-1):
#         for y in range(mem,app_list[i][1]-1,-1):
#             dp[j][y] = max(dp[j][y], dp[j-app_list[i][0]][y-app_list[i][1]] + app_list[i][2])
# print(dp[disk][mem])


s = [1, 4, 2, 2, 3, 3, 2, 4, 1]
res = 0
from collections import defaultdict
class test:
    def __init__(self):
        self.res = 0

    def dfs(self,s,score,flag):
        if not flag:
            if score > self.res:
                self.res = score
            return
        count = 0
        keyi = {}
        for i in range(len(s)):
            if s[i] == s[i-1]:
                flag = True
                keyi[i] = 2
