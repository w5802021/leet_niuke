#链接：https://leetcode.com/problems/longest-consecutive-sequence/
#连续子序列  3,4,5,6,7,7,8,9 则其连续子序列为 3,4,5,6,7,8,9,
def longestConsecutive(nums):    #方法1 O（nlogn） 先排序，
    if not nums:
        return 0

    nums.sort()

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:   #序列中断
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)

def longestConsecutive2(nums):         #方法2 O（n）

    dic = {}

    max_length = 0
    for num in nums:
        if num not in dic:              #找其左右邻居已经找到的连续子序列数值
            left = dic.get(num - 1, 0)  #如果不存在，则返回0
            right = dic.get(num + 1, 0)

            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length

            dic[num] = cur_length
            dic[num - left] = cur_length
            dic[num + right] = cur_length

    return max_length



if __name__ == '__main__':
    nums = [9,1,4,7,7,3,-1,0,5,8,-1,6]
    print(longestConsecutive2(nums))
