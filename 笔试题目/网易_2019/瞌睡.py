n,k = 6, 3
inters = [1 ,3 ,5 ,2 ,5 ,4]
T = [1, 1, 0 ,1, 0 ,0]

cur_ep = 0
point = 0
max_ep = 0
for i in range(n):
    get_p = inters[i]
    if T[i] == 1:
        point += get_p
    else:
        # 当前打瞌睡的总兴趣分
        cur_ep += get_p
    # 使得cur_ep始终只包括k项打瞌睡的总兴趣分
    if i + 1 > k:
        de_ep = inters[i-k] if T[i-k] == 0 else 0
        cur_ep -= de_ep
    #     
    if cur_ep > max_ep:
        max_ep = cur_ep
point += max_ep
print(point)






# max_inters = float('-inf')
# bianli = []
# for i,t in enumerate(T):
#     if t == 0:
#         bianli.append(i)
#
# for i in bianli:
#     if i == 0:
#         tt = 0
#         if i + 1 + k < len(T):
#             r = i + 1 + k
#         else:
#             r = len(T)
#         for j in range(i+1, i+1 + k):
#             if T[j] == 0:
#                 tt += inters[j]
#     elif i == len(inters):
#         tt = inters[-1]
#     else:
#         tt = 0
#         if i + k < len(T):
#             r = i + k
#         else:
#             r = len(T)
#         for j in range(i,r):
#             if T[j] == 0:
#                 tt += inters[j]
#
#     if tt > max_inters:
#         max_inters = tt
#         max_i = i
#
# res = 0
# i = 0
# while i < len(T):
#     if i != max_i:
#         if T[i] == 1:
#             res += inters[i]
#         i += 1
#     else:
#         if i + k < len(T):
#             r = i + k
#         else:
#             r = len(T)
#         res += sum(inters[i:r])
#         i += k
# print(res)




