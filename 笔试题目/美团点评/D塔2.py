T = int(input())

for _ in range(T):
    s = int(input())
    n,d,x,y = map(int, input().split())
    t0,t1,t2 = map(int, input().split())

    count0 = 0
    count1 = 0
    count2 = 0

    while s > 0 :
        if count0 == 0:
            s -= n*d
            count0 = t0
            if s <= 0:
                print('NO')
                break

        if count1 == 0:
            s -= y
            count1 = t1
            if s <= 0:
                print('YES')
                break
        if count2 == 0:
            s -= x
            count2 = t2
            if s <= 0:
                print('YES')
                break
        count0 -= 1
        count1 -= 1
        count2 -= 1




