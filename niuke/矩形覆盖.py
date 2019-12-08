def rectCover(number):
    '''
    斐波那契数列
    '''
    n = number
    if n == 0:
        return 0
    if n == 1:
        return 1
    fir = 1
    las = 2
    for i in range(2, n):
        fir, las = las, fir + las
    return las