def selectsort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
        if i != min:
            list[i],list[min] = list[min],list[i]

    return list

if __name__ == '__main__':
    l = [1, 3, 2, 4, 5, 6, 7, 90, 21, 23, 45]
    print(selectsort(l))
