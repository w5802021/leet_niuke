def IsContinuous(numbers):
    if not numbers:
        return []
    n = len(numbers)
    nums = numbers
    nums.sort()
    countgap = 0
    countzero = 1 if nums[0] == 0 else 0

    for i in range(1,n):
        if nums[i] != 0 and nums[i] == nums[i - 1]:
            return False
        elif nums[i-1] != 0:
            countgap += nums[i] - nums[i-1] - 1
        elif nums[i] == 0:
            countzero += 1
    return False if countgap > countzero else True
nums = [0,3,5,4,6]
print(IsContinuous(nums))