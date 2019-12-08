def multiply(num1,num2):
    size1 = len(num1)
    size2 = len(num2)

    int1 = 0
    int2 = 0
    s0 = ord('0')
    for i in range(size1):
        exp = size1 - i - 1
        num = ord(num1[i]) - s0
        int1 += num * (10 ** exp)

    for i in range(size2):
        exp = size2 - i - 1
        num = ord(num2[i]) - s0
        int2 += num * (10 ** exp)

    return str(int1*int2)

if __name__ == '__main__':
    num1 = "2"
    num2 = "3"
    print(multiply(num1,num2))