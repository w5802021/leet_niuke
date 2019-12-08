import collections
#空间占用多，速度慢
def leastInterval(tasks, n):

    dic = {}
    for i in tasks:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1


    dic = sorted(dic.items(),key = lambda x:x[1],reverse=True)
    max_len = 0
    same_count = 0
    for i in dic:
        if i[1] >= max_len:
            max_len = i[1]
            same_count += 1
        else:
            break
    return max((max_len - 1) * (n + 1) + same_count, len(tasks))

def leastInterval2(tasks, n):

    apt = [tasks.count(x) for x in set(tasks)]
    max_len = max(apt)
    same_count = apt.count(max_len)

    return max((max_len - 1) * (n + 1) + same_count, len(tasks))

def leastInterval3(tasks, n):   #优化
    cdict = collections.Counter(tasks)   #dict_value类型 可迭代
    max_len = max(cdict.values())
    same_count = list(cdict.values()).count(max_len)

    return max((max_len - 1) * (n + 1) + same_count, len(tasks))

if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(leastInterval3(tasks, n))