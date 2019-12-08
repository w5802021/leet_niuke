N = 1
S = ['1','1','0','0']
T = ['1','1','0','0','1','1']


for t in range(N):
    new = []
    for i in S:
        if i == '1':
            new.append('0')
        else:
            new.append('1')
    new = ''.join(new).lstrip('0')
    S = ''.join(S)
    T = ''.join(T)
    if S + new == T:
        print('YES')
    else:
        print('NO')


