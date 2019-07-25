##########################数组操作#########################

def removeElement(nums,val):
    n = len(nums)
    for i in range(n-1,-1,-1):
        if nums[i] == val:
            del nums[i]     #删除元素 del 比 pop  快
    return len(nums)

def removeElement2(nums,val):     #python2 中快
    for i in range(nums.count(val)):
        nums.remove(val)
    return len(nums)

if __name__ ==  '__main__':
    nums =  [3,2,2,3]
    val = 2
    print(removeElement2(nums,val))