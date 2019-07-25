def bubblesort(list):
    flag = True
    for i in range(len(list)):
        if flag:
            flag = False              #初始化为False
            for j in range(i+1,len(list)):
                if list[j] > list[j+1]:
                    list[j],list[j+1] = list[j+1],list[j]   #如何数组发生了交换，这说明无序，还需遍历后面的i 否则说明已经有序
                    flag = True
        else:
            break
    return list

if __name__ == '__main__':
    l = [1, 3, 2, 4, 5, 6, 7, 90, 21, 23, 45]
    print(bubblesort(l))