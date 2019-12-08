def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    er = n
    count = 0
    while er:
        if er % 2 == 1:
            count += 1
        er = er >> 1
    return count

if __name__ == '__main__':

    n = 0b00000000000000000000000000001011
    print(hammingWeight(n))