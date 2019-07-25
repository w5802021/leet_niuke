
def canCompleteCircuit(gas, cost):
    st = 0
    tmp = 0
    minv = 0

    for i in range(len(gas)):
        tmp += gas[i] - cost[i]

        if tmp < minv:      #即找到一点i  使得在该处出发到下一处，油量可以继续维持走下去，否则下一索引，它能
            minv = tmp
            st = i + 1
    return -1 if tmp < 0 else st

if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas,cost))

#问题1: 为什么应该将起始站点设为k+1？
#因为k->k+1站耗油太大，0->k站剩余油量都是不为负的，每减少一站，就少了一些剩余油量。所以如果从k前面的站点作为起始站，剩余油量不可能冲过k+1站。

#问题2: 为什么如果k+1->end全部可以正常通行，且rest>=0就可以说明车子从k+1站点出发可以开完全程？
#因为，起始点将当前路径分为A、B两部分。其中，必然有(1)A部分剩余油量<0。(2)B部分剩余油量>0。
#所以，无论多少个站，都可以抽象为两个站点（A、B）。(1)从B站加满油出发，(2)开往A站，车加油，(3)再开回B站的过程。
#重点：B剩余的油>=A缺少的总油。必然可以推出，B剩余的油>=A站点的每个子站点缺少的油。