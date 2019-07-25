
def strStr1(haystack, needle):
    if not needle in haystack:
        return -1
    return haystack.index(needle)

def strStr2(haystack, needle):
    return haystack.find(needle)

def strStr3(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

if __name__ == '__main__':
    a = "aaaaa"
    b = "a"
    print(strStr1(a,b))