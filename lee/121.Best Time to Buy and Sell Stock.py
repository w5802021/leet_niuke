
def maxProfit(prices):            ######第一次的代码超时，因为自己在一个随着for循环不断增加的列表 采用min（）操作
    res = 0
    if len(prices) <= 1:
        return 0
    minpr = prices[0]
    for i in range(len(prices)):
        diff = prices[i] - minpr
        minpr = min(minpr, prices[i])
        if diff > res:
            res = diff
    return res

##############################122##############################

def maxProfit2(prices):                  ###波峰波谷判断转化计算法
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


if __name__ == '__main__':
    nums = [7,6,4,3,9]
    print(maxProfit(nums))