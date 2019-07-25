def twoCitySchedCost(costs):                                  #sorted() 排序的lambda trick
    costs = sorted(costs, key=lambda x: x[0] - x[1])

    res, N = 0, len(costs) // 2

    # for i in range(N):
    #     res += costs[i][0] + costs[i+N][1]
    return sum(costs[i][0] for i in range(N)) + sum(costs[i + N][1] for i in range(N))

if __name__ == '__main__':
    cost = [[10,20],[30,200],[400,50],[30,20]]
    print(twoCitySchedCost(cost))