def reOrderArray(array):
    '''
    O(1)的空间复杂度     若在开新数组需要O(n)的时间复杂度
    '''
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0:
            if (array[j + 1] % 2 != 0) and (array[j] % 2 == 0):
                array[j + 1] = array[j]
                array[j] = key
            j -= 1
    return array

