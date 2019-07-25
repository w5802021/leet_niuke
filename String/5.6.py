def Capitalorder(ch):
    '''
    :param ch:
    :return:
    '''

    first = 0
    last = len(ch)-1

    while first < last:
        if 'a' <= ch[first] <= 'z' and first < last:
            first += 1
        if 'A' <= ch[last] <= 'Z' and first < last:
            last -= 1
        ch[first],ch[last] = ch[last],ch[first]
    a = ch[:first]
    b = ch[first:]
    a.sort()
    b.sort()
    a.extend(b)

    return a

if __name__ == '__main__':
    ch = list('AbcDef')
    print(Capitalorder(ch))