#########################
#                       #
#找到数组中的最大值和最小值#
#                       #
#########################

def getmaxmin(nums):   #方法1：蛮力法   O(2n-2)
    max = -2**31
    min = 2**31
    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return max,min

def getmaxmin1(nums,l,r):  #分治法   O(3n/2-2)
    if not nums:
        return []

    list = []
    m = (l+r)//2
    if l == r:                   #若数组为奇数个，就有一个单独的元素需要处理
        list.append(nums[l])
        list.append(nums[l])
        return list

    if l+1 == r:                 #为一对时
        if nums[l] >= nums[r]:
            max = nums[l]
            min = nums[r]
        else:
            min = nums[l]
            max = nums[r]
        list.append(min)
        list.append(max)

    ll = getmaxmin1(nums,l,m)
    rl = getmaxmin1(nums,m+1,r)

    Max = ll[1] if ll[1] > rl[1] else rl[1]
    Min = ll[0] if ll[0] < rl[0] else rl[0]

    list.append(Min)
    list.append(Max)
    return list

if __name__ == '__main__':
    nums = [7,3,19,40,4,7,1]
    print(getmaxmin1(nums,0,len(nums)-1))