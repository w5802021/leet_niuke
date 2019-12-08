# def main(l,r):
#     sub = list(seq[l:r + 1])
#     i = 0
#     score = 0
#     stack = []
#     flag = ''
#     while 0 <= i < len(sub):
#         if flag == "" and sub[i] not in "<>":
#             score += int(sub[i])
#             sub[i] = str(int(sub[i]) - 1)
#             stack.append(int(sub[i]))
#             i += 1
#         elif flag == "" and sub[i] == "<":
#             score += sum(stack)
#             return score
#         elif flag == '' and sub[i] == ">":
#             flag += sub[i]
#             idx = i
#             i += 1
#             stack = []
#         elif flag == ">" and sub[i] not in "<>":
#             stack.append(int(sub[i]))
#             sub[i] = str(int(sub[i]) - 1)
#             i += 1
#             if i == len(sub):
#                 score += sum(stack)
#                 return score
#         elif flag == ">" and sub[i] == ">":
#             score += sum(stack)
#             stack = []
#             idx = i
#             i += 1
#         elif flag == ">" and sub[i] == "<":
#             maxx = max(stack)
#             for j in stack:
#                 tmp = ((1 + j) * j) // 2
#                 score += tmp
#             if maxx % 2 == 0:
#                 sub = sub[:idx + 1] + sub[i + 1:]
#                 i = idx + 1
#                 flag = ">"
#             else:
#                 sub = sub[:idx] + sub[i:]
#                 i = idx - 1
#                 flag = "<"
#             stack = []
#         elif flag == "<" and sub[i] not in "<>":
#             stack.append(int(sub[i]))
#             sub[i] = str(int(sub[i]) - 1)
#             i -= 1
#             if i == -1:
#                 score += sum(stack)
#                 return score
#         elif flag == "<" and sub[i] == "<":
#             score += sum(stack)
#             stack = []
#             i -= 1
#         elif flag == "<" and sub[i] == ">":
#             maxx = max(stack)
#             for j in stack:
#                 tmp = ((1 + j) * j) // 2
#                 score += tmp
#             if maxx % 2 != 0:
#                 sub = sub[:i + 1] + sub[idx + 1:]
#                 i += 1
#                 flag = ">"
#             else:
#                 sub = sub[:i] + sub[idx:]
#                 i -= 1
#                 flag = "<"
#             stack = []
#     return score
# if __name__ == '__main__':
#     # n,m,q = map(int,input().split())
#     n, m, q = 4,10,6
#     # seq = [c for c in input().split()]
#     seq = ">22<"
#     lr = [[1,4],[1,3],[2,4],[2,3],[1,1],[2,2]]
#     for a in lr:
#         # a,b = map(int,input().split())
#         l = a[0] - 1
#         r = a[1] - 1
#         if seq[l] == "<":
#             print(0)
#         elif l == r:
#             if seq[l] not in "<>":
#                 print(seq[l])
#             else:
#                 print(0)
#         else:
#             print(main(l,r))

def main(l,r):
    sub = list(seq[l:r + 1])
    i = 0
    score = 0
    stack = []
    flag = ''
    while 0 <= i < len(sub):
        ####### 还未有标志位的处理
        if flag == "" and sub[i] not in "<>":
            score += int(sub[i])
            sub[i] = str(int(sub[i]) - 1)
            stack.append(int(sub[i]))
            i += 1
        elif flag == "" and sub[i] == "<":
            score += sum(stack)
            return score
        elif flag == '' and sub[i] == ">":
            flag += sub[i]
            idx = i
            i += 1
            stack = []
        ########## 标志位为">"
        elif flag == ">" and sub[i] not in "<>":
            stack.append(int(sub[i]))
            sub[i] = str(int(sub[i]) - 1)
            i += 1
            if i == len(sub):
                score += sum(stack)
                return score
        elif flag == ">" and sub[i] == ">":
            score += sum(stack)
            stack = []
            idx = i
            i += 1
        elif flag == ">" and sub[i] == "<":
            # 根据stack里最大的数值来判断删除">"还是"<"
            maxx = max(stack)
            for j in stack:
                tmp = ((1 + j) * j) // 2
                score += tmp
            if maxx % 2 == 0:
                sub = sub[:idx + 1] + sub[i + 1:]
                i = idx + 1
                flag = ">"
            else:
                sub = sub[:idx] + sub[i:]
                i = idx - 1
                flag = "<"
            stack = []
        ########### 标志位为"<"
        elif flag == "<" and sub[i] not in "<>":
            stack.append(int(sub[i]))
            sub[i] = str(int(sub[i]) - 1)
            i -= 1
            if i == -1:
                score += sum(stack)
                return score
        elif flag == "<" and sub[i] == "<":
            score += sum(stack)
            stack = []
            i -= 1
        elif flag == "<" and sub[i] == ">":
            # 根据stack里最大的数值来判断删除">"还是"<"
            maxx = max(stack)
            for j in stack:
                tmp = ((1 + j) * j) // 2
                score += tmp
            if maxx % 2 != 0:
                sub = sub[:i + 1] + sub[idx + 1:]
                i += 1
                flag = ">"
            else:
                sub = sub[:i] + sub[idx:]
                i -= 1
                flag = "<"
            stack = []
    return score
if __name__ == '__main__':
    n,m,q = map(int,input().split())
    seq = [c for c in input().split()]
    for _ in range(q):
        a,b = map(int,input().split())
        l = a - 1
        r = b - 1
        if seq[l] == "<":
            print(0)
        elif l == r:
            if seq[l] not in "<>":
                print(seq[l])
            else:
                print(0)
        else:
            print(main(l,r))














