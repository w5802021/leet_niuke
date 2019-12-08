def count(ss, n, s):
    length = len(ss)
    m = n % length
    if m == 0:
        if ss *(n//length) == s:
            return 1
        else:
            return 0
    for i in range(length, n-m, length):
        if s[i-length: i] != ss:
            return 0
    if s[n-m:] != ss[:m]:
        return 0
    return 1

n = int(input())
s = input()
m = int(input())
sub = []
for i in range(m):
    sub_str = input()
    sub.append(sub_str)
res = 0
for ss in sub:
    res += count(ss, n, s)
print(res)