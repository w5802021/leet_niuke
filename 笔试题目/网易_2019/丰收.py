# 堆数
n = 10
# 第i堆的苹果数
app_heap = [155, 926, 296, 237, 24, 546, 271, 726 ,274,802]

#询问数
m = 7
ques = [1622, 1274, 883, 4224, 4093, 669, 459]

que = sorted(ques)
dic = {}
for i in que:
    dic[i] = int()

res = []
summ = 0
i = 0
for ind,heapnum in enumerate(app_heap):
    summ += heapnum
    while i <= len(que):
        if summ >= que[i]:
            dic[que[i]] = ind+1
            i += 1
            if i == len(que):
                break
        else:
            break
for i in ques:
    print(dic[i])