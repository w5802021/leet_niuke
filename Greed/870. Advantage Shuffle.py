

def advantageCount1(A, B):    #思路将A,B升序排序，并建立由sorteB 到 B的索引映射， 对sortA 大于 sortB的，结果记录在sortb的当前位置记录，否则将其放到sortB的最后位置
    n = len(A)
    sortA = sorted(A)

    res = [0] * n

    idx = sorted(range(n), key=lambda x: B[x])
    sorteB = [B[x] for x in idx]

    bf, af = 0, n - 1
    for a in sortA:
        if a > sorteB[bf]:
            res[idx[bf]] = a    #idx[bf] 是现在B中索引bf  对应在  B排序前中索引的位置
            bf += 1
        else:
            res[idx[af]] = a
            af -= 1
    return res


if __name__ == '__main__':
    A = [2,0,4,1,2]
    B = [1,3,0,0,2]
    print(advantageCount1(A,B))