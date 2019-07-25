def intervalIntersection(A, B):
    def solve(l1, l2):
        maxa = max(l1)
        mina = min(l1)
        maxb = max(l2)
        minb = min(l2)

        if mina < minb:
            if maxa < minb:
                return None,'l1'
            elif maxa <= maxb:
                return [minb, maxa],'l1'
            else:
                return [minb, maxb],'l2'

        elif minb <= mina <= maxb:
            if maxa <= maxb:
                return [mina, maxa],'l1'
            elif maxa > maxb:
                return [mina, maxb],'l2'
        else:
            return None,'l2'

    res = []
    i,j=0,0
    while i < len(A) and j < len(B):
        s = solve(A[i], B[j])
        if s[0] != None:
            if s[1] == 'l1':
                res.append(s[0])
                i += 1
            else:
                res.append(s[0])
                j += 1
        elif s[0] == None:
            if s[1] == 'l1':
                i += 1
            else:
                j += 1
    return res

#思路：如果 A[0] 拥有最小的末端点，那么它只可能与 B[0] 相交。然后我们就可以删除区间 A[0] 了，因为它不能与其他任何区间再相交了。
#     相似的，如果 B[0] 拥有最小的末端点，那么它只可能与区间 A[0] 相交，然后我们就可以将 B[0] 删除了，因为它无法再与其他区间相交了。

def intervalIntersection1(A, B):

    i, j, res = 0, 0, []
    while i < len(A) and j < len(B):
        #两集合无交集
        if A[i][1] < B[j][0]:   #A.max < B.min
            i += 1              #移动A
        elif B[j][1] < A[i][0]: #B.max < A.min
            j += 1              #移动B
        # 两集合有交集
        else:
            res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] > B[j][1]: #A.max > B.max
                j += 1            #移动B（移动终端节点小的）
            else:
                i += 1
    return res

if __name__ == '__main__':
    A = [[3, 5], [9, 20]]
    B = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    print(intervalIntersection1(A, B))