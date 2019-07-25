def findJudge( N, trust):
    '''
    思路：将每个人看成网络的一个节点 a信任b看成是a到b的有向路径 因此记录节点的入度既能判断某人是否是法官
    :param N:
    :param trust:
    :return:
    '''
    rec = [0] * (N + 1)
    for item in trust:
        rec[item[1]] += 1
        rec[item[0]] -= 1
    for i in range(1, N + 1):
        if rec[i] == N - 1:
            return i
    return -1

if __name__ == '__main__':
    N = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    print(findJudge(N, trust))