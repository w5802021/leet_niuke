def strtoint(ch):
    if ch == None:
        flag = False
        print('不是数字')
        return
    flag = True
    minus = False
    res = 0
    i = 0
    if ch[0] == '-':
        minus = True
        i += 1
    if ch[0] == '+':
        i += 1

    for i in range(i,len(ch)):
        if '0'<=ch[i]<='9':
            res = res*10 + int(ch[i])
        else:
            flag = False
            print('不是整数')
            return

    return -res if minus else res

if __name__ == '__main__':
    s = list('d4d5s4')
    print(strtoint(s))
