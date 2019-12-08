num = list(input().split(','))
nums1 = num[:-1] + [num[-1].split(';')[0]]
n = int(num[-1].split(';')[1])

nums_ou = []
nums_ji = []
for c in nums1:
    if int(c) % 2 == 0:
        nums_ou.append(int(c))
    else:
        nums_ji.append(int(c))


nums_ou.sort(reverse=True)
nums_ji.sort(reverse=True)

res = nums_ou + nums_ji

print(','.join([str(c) for c in res[:n]]))




