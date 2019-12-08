class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        def MergeSort(lists):
            if len(lists) <= 1:
                return lists
            mid = int(len(lists)/2)
            left = MergeSort(lists[:mid])
            right = MergeSort(lists[mid:])
            r, l = 0, 0
            res = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
                    # count记录逆序对的数量
                    self.count += len(left)-l
            res += right[r:]
            res += left[l:]
            return res
        MergeSort(data)
        return self.count % 1000000007