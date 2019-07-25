########################45##########################
def Jump(nums):             #想象成这一步所能跳跃的范围，若最后终点在范围内则为最佳点    采用贪心算法   最优避免DP规划导致多余计算

    n,fir,end,count=len(nums),0,0,0   #count计步器             思路：fir0,end0中找到使其跳的最远的作为end1,fir1=end0+1,依照此规律知道某段firn,endn中的数超过n-1

    while end < n-1:     #n-1表示从0到len（nums）要完成的最少跳跃步数
        count = count + 1
        maxend = end + 1
        for i in range(fir, end+1):
            if i + nums[i] >= n - 1:
                return count
            maxend = max(i + nums[i], maxend)
        fir, end = end + 1 , maxend       #下一轮的开始为上一轮while循环的结束
    return count

def Jump2(nums):                       #####以上程序碰到列表中有0的数则可能出现问题
    last, cur, step = 0, 0, 0
    n = len(nums)

    for i in range(n):

        if i > last:
            step += 1
            last = cur
        cur = max(cur, i + nums[i])

    return step
##############################55###############################
def canJump(nums):
    maxend = 0
    for i in range(len(nums)):      #前序遍历
        if i > maxend:
            return False

        maxend = max(i+nums[i],maxend)
    return True

def canJump2(nums):
    n = len(nums) -1
    goal = nums[n]
    for i in range(n,-1,-1):         #后序遍历
        if i + nums[i] >= goal:
            goal = i
    return not goal

if __name__ == '__main__':
    nums = [0,2,3]
    nums2 = [3,2,1,0,4]
    print(canJump(nums))