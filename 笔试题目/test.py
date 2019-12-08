
# X = [5,13,4]
# Y = [2,7,12]
# Z = ['113221101000101','1016','2222248A']
T = int(input())
def func(x,y,z):
    x = int(x)
    y = int(y)
    for i in range(1,len(z)):
        try :
            valx = int(z[:i],x)
            valy = int(z[i:],y)
        except:
            continue
        if valx == valy:
            return valx

for i in range(T):
    a = [x for x in input().split()]
    X,Y,Z = a[0],a[1],a[2]
    print(func(X,Y,Z))






