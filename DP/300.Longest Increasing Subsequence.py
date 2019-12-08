class DP:

    def lengthOfLIS(self, nums):
        '''
        方法： 动态规划o（n^2）
        :param nums:
        :return:
        '''
        if len(nums) < 2:
            return len(nums)
        # 1、确定状态，dp[i]表示nums[:i]这段数组的最长上升子序列
        # 2、初始化
        dp = [1] * len(nums)
        # 4、计算顺序 自左往右
        for i in range(1, len(nums)):
            # j为遍历i之前的数
            for j in range(i):
                # 遍历i之前的所有dp，判断前面dp[j]+1 是否有长于dp[i]的
                if nums[i] > nums[j]:
                    # 2、状态转移方程
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def lengthOfLIS2(self, nums):
        '''
         方法: 动态规划 + 二分查找 o（nlogn）
         思路：模拟一个stack，每输入一个数x，如果这个数大于栈顶的那个数，把它推入栈中，
         如果不是，则用二分查找栈中元素是否有小于该元素的值，如果存在，则将x插入到它的后面
         虽然插入后改变了栈中元素的值，最长上升子序列的输出不合理，但是对于求出最长上升子序列的长度不影响
        :param nums:
        :return:
        '''
        # stack是一个逐个存储nums的有序栈
        stack = [0] * len(nums)
        # 1、确定状态 当前迭代的最大长度
        maxl = 0

        # 4、计算顺序  自左向右
        for x in nums:
            # 3、初始边界条件
            # 当x不符合上升子序列时，maxl的值会减小，从而缩短了二分搜索的范围
            low, high = 0, maxl
            # 在stack中（二分搜索）找到一个位置插入x
            while low < high:
                mid = low +(high - low) // 2
                if stack[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            # stack[:low]的长度  即为以x为子序列末尾的最大长度
            stack[low] = x
            # 2、状态转移方程
            maxl = max(low + 1, maxl)
        return maxl

if __name__ ==  '__main__':
    mal = DP()
    nums = [4, 12, 17, 18, 20, 15, 101, 18]
    print(mal.lengthOfLIS2(nums))
