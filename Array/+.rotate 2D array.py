def rotate(arr):
    lens = len(arr)
    i = lens - 1
    res = []

    while i > 0:      #打印右上角
        row,col = 0,i
        tem1 = []
        while col < lens:
            tem1.append(arr[row][col])
            row += 1
            col += 1
        res.append(tem1)

        i -= 1

    i = 0
    while i < lens:   #打印左下角
        row,col = i,0
        tem2 = []
        while row < lens:
            tem2.append(arr[row][col])
            row += 1
            col += 1
        res.append(tem2)

        i += 1
    return res

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate(arr))


