def insertsort(list):
    for i in range(1,len(list)):
        key = list[i]   #当前要插入的数
        j = i - 1       #j为前一个插入的数的索引
        while j >= 0:   #遍历前面所有已排序好的数 ，找到可插入的位置
            if key < list[j]:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1
    return list

if __name__ == '__main__':
    l = [1, 3, 4, 5, 6, 2, 7, 90, 21, 23, 45]
    print(insertsort(l))