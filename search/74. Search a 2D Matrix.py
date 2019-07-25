import bisect

def searchMatrix(matrix, target):
    for arr in matrix:
        ind = bisect.bisect_left(arr, target)
        if not ind < len(arr):
            continue
        if arr[ind] == target:
            return True
    return False

def searchMatrix2(matrix, target):    ##先快速选到合适行，在选到合适列
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    i = m - 1   #行
    j = 0       #列   ##从左下角出发  也可选择从右上角 i = 0 , j = n-1
    while i >= 0 and j < n:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1
    return False

if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(searchMatrix2(matrix, target))