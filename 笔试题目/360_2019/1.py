N = int(input())
class pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
pairs = []
for i in range(N):
    a1,a2 = map(int, input().split())
    pairs.append(pair(a1,a2))
xmin = float('-inf')
xmax = float('inf')
ymin = float('-inf')
ymax = float('inf')
for pair in pairs:
   if pair.x < xmin:
       xmin = pair.x
   if pair.x > xmax:
       xmax = pair.x
   if pair.y < ymin:
       ymin = pair.y
   if pair.y > ymax:
       ymax = pair.y
if xmax - xmin > 0 and ymax - ymin == 0:
    print((xmax-xmin)**2)
elif ymax - ymin > 0 and xmax - xmin == 0:
    print((ymax - ymin) ** 2)
else:
    if ymax - ymin <  xmax - xmin:
        print((ymax - ymin) ** 2)
    else:
        print((xmax - xmin) ** 2)