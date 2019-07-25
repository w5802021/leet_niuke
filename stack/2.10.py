class pair():
    def __init__(self,a=None,b=None):
        self.a = a
        self.b = b

def findpais(arr):
    dic = dict()
    n = len(arr)
    res = []
    for i in range(n):
        for j in range(i+1,n):
            summ = arr[i] + arr[j]
            if summ not in dic:
                dic[summ] = pair(arr[i],arr[j])
            else:
                res.append([(dic[summ].a,dic[summ].b),(arr[i],arr[j])])
    return res
if __name__ == '__main__':
    arr = [3,4,7,10,20,9,8]
    print(findpais(arr))