
ss = input()
res = ''
count = 0
for i in range(len(ss)):
    if 0<i<len(ss)-1:
        if ss[i] == ss[i-1]:
            count += 1
        else:
            if count-1 != 0:
                res += str(count-1)
            res += ss[i-1]
            count = 1
    elif i == 0:
        count += 1
    elif i == len(ss) - 1:
        if ss[i] == ss[i-1]:
            count += 1
            if count - 1 != 0:
                res += str(count-1)
            res += ss[i]
        else:
            if count - 1 != 0:
                res += str(count-1)
            res += ss[i - 1]
            res += ss[i]

print(res)
