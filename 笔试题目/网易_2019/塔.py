n,k = 3,2
class tower:
    def __init__(self,id,h):
        self.id = id
        self.h = h

towers = [tower(i,int(c)) for i,c in enumerate([5,8,5])]
res = []
for i in range(k):
    max_ind = towers.index(max(towers, key=lambda x: x.h))
    min_ind = towers.index(min(towers, key=lambda x: x.h))
    res.append([max_ind+1, min_ind+1])

    towers[max_ind].h -= 1
    towers[min_ind].h += 1

    if max(towers, key=lambda x: x.h).h - min(towers, key=lambda x: x.h).h < 2:
        break
print("%d %d" % (max(towers, key=lambda x: x.h).h - min(towers, key=lambda x: x.h).h, len(res)))
for i in range(len(res)):
    print("%d %d" % (res[i][0], res[i][1]))




