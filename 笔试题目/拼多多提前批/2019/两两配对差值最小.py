def main(n,nums):
    nums.sort()
    mid = len(nums) // 2
    num1 = nums[:mid]
    num2 = nums[mid:]
    for i in range(mid):
        num1[i] = num1[i] + num2[-(i+1)]
    maximum = max(num1)
    minimum = min(num1)
    return maximum - minimum

if __name__ == '__main__':
    n = int(input())
    nums = [int(c) for c in input().split()]
    print(main(n,nums))