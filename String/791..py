import collections
def customSortString(S, T):
    c = collections.Counter(T)       #记录待排序字符串各字符出现次数
    res = []
    for i in T:
        if i not in S:
            res.append(i)
    for i in S:
        res.extend([i] * c[i])
    return ''.join(res)

if __name__ == '__main__':
    S ='cba'
    T = 'abcd'
    print(customSortString(S,T))