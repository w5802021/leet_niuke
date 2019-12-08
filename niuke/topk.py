######
# 类快速排序求topk
######
class sol():
    def __init__(self):
        self.res = []

    def partion(self,arr,low,high):
        pivot = arr[low]
        while low < high:
            while low < high and arr[high] >= pivot:
                high -= 1
            arr[low] = arr[high]

            while low < high and arr[low] <= pivot:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot
        return low

    def topk(self,nums,k):
        '''
        找到第k个最小的元素
        :param nums:
        :return:
        '''
        if not nums or len(nums) < k or k == 0:
            return []
        low = 0
        high = len(nums) - 1
        p = self.partion(nums,low,high)
        while p != k - 1:
            if p < k-1:
                low = p + 1
            else:
                high = p - 1
            p = self.partion(nums,low,high)
        res = []
        for i in range(p+1):
            res.append(nums[i])
        return res

    def main(self):
        nums = [4,5,1,6,2,7,3,8]
        k = 6
        return self.topk(nums,k)

test = sol()
print(test.main())


