import itertools

def countAndSay(n):     #####这一题关键要读懂题目，后一个序列的输出结果是对前面的序列每个位置的数的描述，存在两个及以上连续的相同的数，则要计数报数
    st = '1'                ###
    count = 1

    for i in range(n - 1):
        tmp = ''
        for j in range(len(st) - 1):
            if st[j] == st[j + 1]:
                count += 1
            else:
                tmp += str(count)
                tmp += st[j]
                count = 1
        tmp += str(count)
        tmp += st[-1]
        count = 1
        st = tmp

def countAndSay2(n):
    st = '1'

    for i in range(n-1):

        a = [digit for digit, group in itertools.groupby(st)]
        b = [len(list(group)) for digit, group in itertools.groupby(st)]   #itertools groupby 将迭代器中相邻的重复元素跳出来放在一起
        st = ''.join(str(len(list(group))) + digit for digit,group in itertools.groupby(st))
    return st

if __name__ == '__main__':
    n = 10
    print(countAndSay2(n))