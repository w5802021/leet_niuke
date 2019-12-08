n = int(input())
Ex = 0
for i in range(n):
    xi,pi = map(int,input().split())
    Ex += xi*pi/100
Ex = round(Ex,3)
print('%.3f' %Ex)