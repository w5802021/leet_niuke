
def canPlaceFlowers(flowerbed, n):    ####列表两个表头00的情况   表尾00的情况  ####
    nums = flowerbed
    res = 0

    nums.insert(0, 0)    ##在其前和后添加10 01
    nums.insert(0, 1)
    nums.append(0)
    nums.append(1)
    count = 0

    for i in nums:
        if i == 1:
            res += abs(count - 1)//2
            count = 0
        else:
            count += 1
    res += abs(count - 1) // 2
    return  res >= n

if __name__ == '__main__':
    flowerbed = [0,1,1,0,1,0,1,0,0]
    n = 1
    print(canPlaceFlowers(flowerbed,n))