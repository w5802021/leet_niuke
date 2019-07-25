#如果要对数组区间 [p, r] 的数据进行排序，我们先选择其中任意一个数据作为 pivot（分支点），一般为区间最后一个元素
#然后遍历数组，将小于 pivot 的数据放到左边，将大于 pivot 的数据放到右边。接着，我们再递归对左右两边的数据进行排序，
#直到区间缩小为 1 ，说明所有的数据都排好了序。
#
#

def quicksort(list,left,right):
    if left < right:
        q = partition(list,left,right)   #q 为分好区后，pivot的索引位置
        quicksort(list,left,q-1)
        quicksort(list,q+1,right)

def partition(arr,low,high):    # 【low,high】为数组索引边界  partition函数作用：选中pivot，将它放在一个位置，使得它左边的值比它小，右边的值比它大
    pivot = arr[low]            #分支点选为数组最左边的点  ，这个可根据实际情况选择
    while low < high:
        while low < high and arr[high] >= pivot:  #一次尽量多找到数组中连续的数都大于pivot  >=是因为将多余的pivot放入区域
            high -= 1

        arr[low] = arr[high]                     #将小于pivot的数放到另一分区前面

        while low < high and arr[low] <= pivot:     #一次尽量多找到数组中连续的数都小于pivot    可以写<= ？
            low += 1

        arr[high] = arr[low]                        #将大于pivot的数放到另一分区前面

    arr[low] = pivot     #low=high，此位置存pivot

    return low  #返回pivot的下标位置

if __name__ == '__main__':
    l = [8, 3, 2, 4, 5, 6, 7, 90, 21, 23, 8]
    quicksort(l,0,len(l)-1)
    print(l)
