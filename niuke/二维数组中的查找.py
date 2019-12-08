def Find(target, array):
    # write cod
    m = len(array)
    n = len(array[0])
    i = m - 1
    j = 0
    while i >= 0 and j < n:
        if array[i][j] == target:
            return True
        elif array[i][j] < target:
            j += 1
        else:
            i -= 1
    return False

if __name__ == '__main__':
    target = 10
    mat = [[1,3,5],[6,9,10],[12,15,16]]
    print(Find(target,mat))