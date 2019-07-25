
def rotatesame(str1,str2):
    def issub(str1,str2):
        return str1.find(str2) != -1

    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return False

    tmp = [None] * (len1*2)

    for i in range(len1):
        tmp[i] = str1[i]
        tmp[i+len1] = str1[i]

    return issub(''.join(tmp),str2)

if __name__ == '__main__':
    str1 = 'waterbottle'
    str2 = 'erbottlewat'
    print(rotatesame(str1,str2))
