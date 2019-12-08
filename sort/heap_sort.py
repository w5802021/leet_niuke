def heapsort(list):
    # 1、构造大顶堆 2、调整堆将最大值放到最后的节点位置
    n = len(list)
    # 构造大顶堆
    for i in range((n//2),-1,-1):
        adjust_head(list,i,n)
    # 交换堆顶元素与最后一个元素的位置
    for i in range(n-1,-1,-1):
        # 先将为调整的数中的排在数组最后一个的元素放到最前面，
        list[0],list[i] = list[i],list[0]
        # 对nums[0:i]中的数重新建堆
        adjust_head(list, 0, i)

def adjust_head(list,i,lenth):
    # lchild是索引值 i从0开始 堆的索引i从0开始，与大话数据结构定义的不一样
    lchild = 2*i + 1
    rchild = 2*i + 2
    maxl = i
    if i < lenth//2:
        if lchild < lenth and list[lchild] > list[maxl]:
            maxl = lchild
        if rchild < lenth and list[rchild] > list[maxl]:
            maxl = rchild
        if maxl != i:
            # 将当前最大的数移到后面
            list[maxl],list[i] = list[i],list[maxl]
            # 在去除该最大数后的数组中重新构造堆
            adjust_head(list,maxl,lenth)

if __name__ == '__main__':
    l = [1, 3, 2, 4, 5, 6, 7, 90, 21, 23]
    heapsort(l)
    print(l)
