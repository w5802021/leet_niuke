ss = list(input())
res = []
char = ['(', ')', '<']
flag = 0
for i in ss:
    if i not in char:
        if flag == 0:
            res.append(i)
    if i == '(':
        flag += 1
    if i == ')':
        flag -= 1
    if i == '<' and flag==0:
        if len(res) > 0:
            res.pop()

print(''.join(res))