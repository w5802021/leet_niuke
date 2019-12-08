def addStrings(num1, num2):

    res = ""
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0:
        n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
        tmp = n1 + n2 + carry
        carry = tmp // 10
        res = str(tmp % 10) + res
        i, j = i - 1, j - 1
    if carry: res = "1" + res
    return res


if __name__ == '__main__':
    nums1 = '9' * 36
    nums2 = '2' * 36
    print(addStrings(nums1, nums2))
