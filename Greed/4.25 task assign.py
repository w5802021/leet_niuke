def cal_process_time(t,m,n):
    '''
    :param t:每个服务器处理的时间
    :param m:服务器的数量
    :param n:任务个数
    :return:每个服务器的处理任务所花的总时间
    '''

    pro_time = [0]*m

    for i in range(n): #遍历每个任务
        #选择第一个服务器处理
        mintime = pro_time[0] + t[0]
        minind = 0
        #在后续服务器中找到一个使得所需时间最短的
        for j in range(1,m):
            if mintime > pro_time[j] + t[j]:
                mintime = pro_time[j] + t[j]
                minind =j

        pro_time[minind] += t[minind]

    return pro_time

if __name__ == '__main__':
    t = [7,10]
    m = 2
    n = 10
    print(cal_process_time(t,m,n))