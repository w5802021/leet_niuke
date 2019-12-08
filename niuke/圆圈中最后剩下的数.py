class Solution:
    def LastRemaining_Solution(self, n, m):

        if n < 1 or m < 1:
            return -1
        res = 0

        for i in range(2, n):
            res = (res + m) % i
        return res

    def LastRemaining_Solution1(self, n, m):
        '''

        :param n:
        :param m:
        :return:
        '''
        if n < 1 or m < 1:
            return -1
        nums = list(range(n))
        # cur代表当前指针指向环中的某个数
        cur = 0
        while len(nums) > 1:
            for i in range(1,m):
                cur += 1
                if cur == len(nums):
                    cur = 0
            nums.remove(nums[cur])
            if cur == len(nums):
                cur = 0
        return nums
