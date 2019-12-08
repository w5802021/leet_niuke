n,m = 5,3
nums = [1 ,2 ,3 ,2 ,2]
Q = 3
questions = [[1, 4],[2, 4],[1, 5]]
res = []
# questions.sort(key = lambda x:x[0])

for i in range(Q):
    l = questions[i][0]
    r = questions[i][1]
    nums_test = nums[l-1:r]
    see = set(nums_test)
    res.append(len(see))
print('\n'.join(str(c) for c in res))

