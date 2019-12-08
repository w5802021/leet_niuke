#
#内部bisect库实现
#

import bisect
L = [1, 3, 3, 6, 8, 12, 15]
x = 3
# 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１
x_insert_point = bisect.bisect_left(L, x)
print(x_insert_point)
# 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回右侧位置３
x_insert_point = bisect.bisect_right(L, x)
print(x_insert_point)
# 将x插入到列表L中，x存在时插入在左侧
x_insort_left = bisect.insort_left(L, x)
print(L)
# 将x插入到列表L中，x存在时插入在右侧　　
x_insort_rigth = bisect.insort_right(L, x)
print(L)

#
#二完全有序数组的二叉搜索
#

def binary_search(nums,target):
    low, high = 0, len(nums)
    # 没在列表中的元素能插在中间
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low  #若查找的数不在列表中，则返回一个可插入的索引位置，使得列表依旧按顺序排列

#
#非完全有序数组的二叉搜索   eg.[3,4,5,0,1,2]
#

def binary_search2(nums,target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        if nums[low] <= nums[mid]:  # 二分后前半段是升序
            if nums[low] <= target <= nums[mid]:  # 目标在前半段
                high = mid - 1
            else:
                low = mid + 1
        else:  # 二分后前半段不是升序
            if nums[mid] <= target <= nums[high]:  # 目标在后半段
                low = mid + 1
            else:
                high = mid - 1
    return -1
########################二分查找四种#######################
def lower_bound(data,value):
    '''
    第一个大于等于value的位置

    '''
    st = 0
    en = len(data)-1
    mid = st+((en-st)>>1)
    while(st<=en):
        if data[mid]<value:
            st = mid +1
        else:
            en = mid -1
        mid = st+((en-st)>>1)
    return st
def lower_bound_en(data,value):
    '''
    第一个小于value的位置
    '''
    st = 0
    en = len(data)-1
    mid = st+((en-st)>>1)
    while(st<=en):
        if data[mid]<value:
            st = mid +1
        else:
            en = mid -1
        mid = st+((en-st)>>1)
    return en
def upper_bound(data,value):
    '''
    第一个大于value的位置

    '''
    st = 0
    en = len(data)-1
    mid = st+((en-st)>>1)
    while(st<=en):
        if data[mid]<=value:
            st = mid +1
        else:
            en = mid -1
        mid = st+((en-st)>>1)
    return st
def upper_bound_en(data,value):
    '''
    第一个小于等于value的位置
    '''
    st = 0
    en = len(data)-1
    mid = st+((en-st)>>1)
    while(st<=en):
        if data[mid]<=value:
            st = mid +1
        else:
            en = mid -1
        mid = st+((en-st)>>1)
    return en

if __name__ == '__main__':
    nums = [1,2,5,12,36,44,49,69,75,79,88,98,100]
    tar = 23
    print(binary_search(nums,tar))