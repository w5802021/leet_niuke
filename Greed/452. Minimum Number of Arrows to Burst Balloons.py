###
#    思路：贪心前一般需要对序列值进行排序，本题的关键是每个序列坐标的end值，根据题意 xstart ≤ x ≤ xend 才能射爆气球，为使得一根箭尽可能
#         多的射爆气球，应该保证交叠区域满足条件 ：任何交叠区域的气球的xstarti < xend1，xend1是该交叠区域最小的xend值
#
###
def findMinArrowShots(points):
    points.sort(key = lambda x:x[1])

    res = 0
    end = -float('inf')
    for p in points:
        if p[0] > end:
            res += 1
            end = p[1]
    return res


if __name__ == '__main__':
    point = [[10,16], [2,8], [1,6], [7,12]]
    print(findMinArrowShots(point))