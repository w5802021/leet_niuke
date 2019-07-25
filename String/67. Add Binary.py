
def addBinary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    binary = lambda n: '' if n == 0 else binary(n // 2) + str(n % 2)

    return binary(a + b) if a + b != 0 else '0'


def addBinary2(a, b):
    a = int(a, 2)
    b = int(b, 2)

    # return bin(a+b)[2:]
    return "{0:b}".format(a+b)           #################二进制与十进制转换

if __name__ == '__main__':
    a = "1010"
    b = "1011"
    print(addBinary2(a,b))

