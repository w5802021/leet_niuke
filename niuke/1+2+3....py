def Sum_Solution(n):
    '''
    短路原理  & 若第一项为0就不会判断后面一项
    :param n:
    :return:
    '''
    # write code here
    res = n
    res = res & (res + Sum_Solution(n - 1))
    return res

print(Sum_Solution(3))