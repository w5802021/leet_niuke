def t1(nums,l,r):
    def partion(nums,l,r):
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    if l < r:
        mid = partion(nums,l,r)
        t1(nums,l,mid-1)
        t1(nums,mid+1,r)
nums = [4,3,25,4]
t1(nums,0,len(nums)-1)
print(nums)

