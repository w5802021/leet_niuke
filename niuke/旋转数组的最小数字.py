class Solution:
    def minNumberInRotateArray(self, rotateArray):
        '''

        :param rotateArray:
        :return:
        '''
        nums = rotateArray
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            # 中间的数大于右边最大的数，说明最小的数应该出现在右半部分
            if nums[mid] > nums[high]:
                low = mid + 1
            # 特殊测试用例 [1,1,1,1,0,1] 此时只能用O(log(n))的算法进行搜索
            elif nums[mid] == nums[high]:
                high = high - 1
                # 或low = low + 1
            else:
                high = mid
        return nums[low]