L,R = map(int,input().split())
L,R = 1,1
import math
C = 2*math.pi*R
L = L%C
# 逆时针
x1 = round(R*math.sin(L/R),3)
y1 = round(R*math.cos(L/R),3)

# 顺时针
x2 = round(R*math.sin(-L/R),3)
y2 = round(R*math.cos(-L/R),3)

print('%.3f' % y2+ ' ' + '%.3f' % x2)
print('%.3f' % y1+ ' ' + '%.3f' % x1)
