def heapsort(list):                 #1、构造大顶堆 2、调整堆将最大值放到最后的节点位置
    lenth = len(list)
    for i in range((lenth//2),-1,-1):      #构造大顶堆
        adjust_head(list,i,lenth)
    for i in range(lenth-1,-1,-1):          #交换堆顶元素与最后一个元素的位置
        list[0],list[i] = list[i],list[0]   #先将为调整的数中的排在数组最后一个的元素放到最前面，
        adjust_head(list, 0, i)

def adjust_head(list,i,lenth):
    lchild = 2*i + 1   #lchild是索引值 i从0开始 堆的索引i从0开始，与大话数据结构定义的不一样
    rchild = 2*i + 2
    maxl = i
    if i < lenth//2:
        if lchild < lenth and list[lchild] > list[maxl]:
            maxl = lchild
        if rchild < lenth and list[rchild] > list[maxl]:
            maxl = rchild
        if maxl != i:
            list[maxl],list[i] = list[i],list[maxl]   #将当前最大的数移动后面
            adjust_head(list,maxl,lenth)              #在去除该最大数后的数组中重新构造堆

if __name__ == '__main__':
    l = [1, 3, 2, 4, 5, 6, 7, 90, 21, 23]
    heapsort(l)
    print(l)
