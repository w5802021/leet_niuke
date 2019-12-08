# 如果要对数组区间[p, r]的数据进行排序，我们先选择其中任意一个数据作为 pivot（分支点），一般为区间最后一个元素
# 然后遍历数组，将小于pivot的数据放到左边，将大于pivot的数据放到右边。接着，我们再递归对左右两边的数据进行排序，
# 直到区间缩小为1，说明所有的数据都排好了序。
#特点：每递归一次，即有一个元素被排在正确的位置上

def qsort(arr):
    '''
    递归方法
    :param arr:
    :return:
    '''
    if not len(arr):
        return []
    else:
    # 在这里以第一个元素为基准线
        pivot = arr[0]
        left = qsort([x for x in arr[1:] if x < pivot])
        right = qsort([x for x in arr[1:] if x >= pivot])
    return left+[pivot]+right

def quicksort(list,left,right):
    #
    if left < right:
        q = partition(list,left,right)   #q 为分好区后，pivot的索引位置
        quicksort(list,left,q-1)
        quicksort(list,q+1,right)

def partition(arr,low,high):
    '''
    [low,high]为数组索引边界
    partition函数作用：选中pivot，使得它左边的值比它小，右边的值比它大，这样，这个pivot就排在了它最后的位置上
    :param arr:
    :param low:
    :param high:
    :return:
    '''
    # 分支点选为数组最左边的点  ，这个可根据实际情况选择
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        # 将小于pivot的数放到另一分区前面
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        # 将大于pivot的数放到另一分区前面
        arr[high] = arr[low]

    # low=high，此位置存pivot
    arr[low] = pivot
    return low  #返回pivot的下标位置

def quick_sort(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            # 下一次循环调整数组中小于pivot的元素
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            # 下一次循环调整数组中大于pivot的元素
            stack.append(r)
            stack.append(index + 1)

if __name__ == '__main__':
    l = [8, 3, 2, 4, 5, 6, 7, 90, 21, 23, 8]
    # l=qsort(l)
    # quick_sort(l)
    quicksort(l,0,len(l)-1)
    print(l)
