class DP:

    def lengthOfLIS(self, nums):    #方法一 动态规划 o（n2）
        if len(nums) < 2:
            return len(nums)

        dp = [1] * len(nums)   #初始化DP数组，表示当前索引位置前（包括索引位置）的数组 的最长上升子序列

        for i in range(1, len(nums)):
            for j in range(i):  # j为遍历i之前的数
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])   #遍历i之前的所有dp，判断前面dp[j]+1 是否有长于dp[i]的

        return max(dp)

    def lengthOfLIS2(self, nums):     #方法二 二分查找 o（nlogn）

        tails = [0] * len(nums)
        size = 0
        for x in nums:                #思路：模拟一个stack，每输入一个数x，如果这个数大于栈顶的那个数，把它推入栈中，
            i, j = 0, size            #如果不是，则用二分查找栈中元素是否有小于该元素的值，如果存在，则将x插入到它的后面
                                      #虽然插入后改变了栈中元素的值，最长上升子序列的输出不合理，但是对于求出最长上升子序列的长度不影响
            while i != j:    #对0-size这段数组进行二份搜索
                mid = (i + j) // 2  #取整
                if tails[mid] < x:    #将非x大于栈顶的元素推入栈
                    i = mid + 1   #将该x插入到后面
                else:
                    j = mid
            tails[i] = x
            size = max(i + 1, size)   #size是nums中首元素到下一个x的长度，
        return size

if __name__ ==  '__main__':
    mal = DP()
    nums = [4, 12, 17, 18, 20, 15, 101, 18]
    print(mal.lengthOfLIS2(nums))
