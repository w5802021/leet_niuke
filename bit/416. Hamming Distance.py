def hammingDistance( x, y):
    z = x ^ y
    count = 0
    while z:
        if z&1 == 1:
            count += 1
        z >>= 1
    return count

if __name__ == '__main__':
    print(hammingDistance( 1, 4))