def nthUglyNumber(n):
    '''
    思路：因为丑数只能由1,2,3,5组合相乘得到，因此（除1外）每个丑数都是由若干个2,3,5的乘子组成
         每次循环找下一丑数都是
    :param n:
    :return:
    '''
    res = [1]
    p2, p3, p5 = 0,0,0
    while n-1 > 0:
        # p2代表res对应第p2之前位置已经乘过p2，且res[p2-1]*2在前面的丑数列表中已经出现
        tmp = min(res[p2]*2,res[p3]*3,res[p5]*5)
        res.append(tmp)
        if res[p2]*2 == tmp:
            p2 += 1
        # 这里注意要用if，不能用elif，
        # 因为丑数6，可能由于丑数2乘以res[p3]产生；也可能由于丑数3乘以res[p2]产生,而丑数6已经在res列表中
        # 若采用elif，p3不会+1，下一次循环时，tmp又会等于6
        if res[p3]*3 == tmp:
            p3 += 1
        if res[p5]*5 == tmp:
            p5 += 1
        n -= 1
    return res[-1]

if __name__ == '__main__':
    n = 10
    print(nthUglyNumber(n))