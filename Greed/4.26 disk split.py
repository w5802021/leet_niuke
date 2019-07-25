def disk_split(d,sp):
    dind = 0

    for i in range(len(sp)):
        while dind < len(d) and d[dind] < sp[i] :   #注意这种情况 ，先判断列表索引满足条件，在调用列表索引，避免报错
            dind += 1

        if dind >= len(d):
            return False

        d[dind] -= sp[i]

    return True

if __name__ == '__main__':
    d = [120,120,120]
    sp = [60,80,80,20,80]
    print(disk_split(d,sp))
