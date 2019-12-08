def FindContinuousSequence(tsum):
    '''
    low，high双指针 动态滑动窗口
    :param tsum:
    :return:
    '''
    res = []
    if tsum == 1:
        return []
    low = 1
    high = 2
    while low < high:
        summ = (low + high)*(high - low + 1) // 2

        if summ == tsum:
            res.append([x for x in range(low, high + 1)])
            low += 1
        elif summ < tsum:
            high += 1
        else:
            # 此时左指针定位的元素开始不能使得凑出和为tsum  故左指针右移
            low += 1
    return res

def FindContinuousSequence1(tsum):

    res=[]
    for i in range(1,tsum//2+1):
        sumRes = i
        for j in range(i+1,tsum//2+2):
            sumRes += j
            if sumRes == tsum:
                res.append(list(range(i, j+1)))
                break
            elif sumRes > tsum:
                break
    return res
