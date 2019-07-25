##条件语句判断，is与==的区别
#is用于判断两个对象是否相同   ==判断是否相等
#is不要用于数值与字符串等不可变的类型
#
def findDuplicate(nums):
    return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))

#######快慢指针方法#####同环形链表二        环的入口为
def findDuplicate1(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:    #找到环
            slow = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow

if __name__ == '__main__':
    nums = [2,3,1, 1]
    print(findDuplicate1(nums))
